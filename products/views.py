import time
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from .models import Product, OrderItem, Client
from .forms import ContactForm, ClientForm
from .utils import special_product


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        product_list = Product.objects.filter(active=True)[:6]
        context = {"product_list": product_list, "form": ContactForm}
        return render(request, "products/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            name = form.cleaned_data["name"]
            email_from = form.cleaned_data["email"]
            phone_no = form.cleaned_data["phone_no"]
            message = f'{form.cleaned_data["comment"]}.\n\nSent by {name}.\nPhone No is {phone_no}.\nEmail is {email_from}'
            receipient_list = [
                settings.EMAIL_HOST_USER,
            ]
            send_mail(
                subject,
                message,
                email_from,
                receipient_list,
                fail_silently=False,
            )
            messages.success(request, "Your message was sent successfully")
            return redirect("products:index")


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "product_list"
    paginate_by = 6

    def get_queryset(self):
        product_list = Product.objects.filter(active=True)
        return product_list


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
    login_url = "account_signup"

    def get_object(self):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        order_item, created = OrderItem.objects.get_or_create(
            product=product, user=user, paid=False
        )
        host = self.request.get_host()
        return_url = (
            f"http://{host}{reverse('products:client_form')}"
            if product.title.title() == "Get Hired"
            and product.is_featured
            and not Client.objects.filter(user=user).exists()
            else f"http://{host}{reverse('payments:payment_completed')}"
        )
        paypal_dict = {
            # "business": settings.PAYPAL_RECEIVER_EMAIL,
            "business": "sb-47n431224883123@business.example.com",
            "amount": order_item.product.price,
            "item_name": order_item.product.title,
            "invoice": str(order_item.id),
            "currency_code": "USD",
            "notify_url": f"http://{host}{reverse('paypal-ipn')}",
            "return": return_url,
            "cancel_return": f"http://{host}{reverse('payments:payment_cancelled')}",
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context["paypal_dict"] = paypal_dict
        context["form"] = form
        if not settings.PAYPAL_TEST:
            context["action"] = "https://www.paypal.com/cgi-bin/webscr"
        else:
            context["action"] = "https://www.sandbox.paypal.com/cgi-bin/webscr"
        return context


class ClientFormView(LoginRequiredMixin, View):
    login_url = "account_signup"

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(title="Get Hired", is_featured=True)
        order_item = OrderItem.objects.filter(
            product=product, user=request.user, paid=True
        )
        if order_item.exists():
            form = ClientForm(
                initial={
                    "name": request.user.name,
                    "email": request.user.email,
                    "phone_no": request.user.phone_no,
                }
            )
            context = {"form": form}
            return render(request, "products/client_form.html", context)
        else:
            context = {"product": product}
            return render(request, "403.html", context)

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone_no = form.cleaned_data.get("phone_no")
            product = special_product()
            client_form = form.save(commit=False)
            request.user.name = name
            request.user.email = email
            request.user.phone_no = phone_no
            request.user.save()
            client_form.user = request.user
            client_form.product = product
            client_form.save()
            messages.success(request, "Your form was submitted successfully!")
            return redirect("products:product_list")
        else:
            context = {"form": form}
            return render(request, "products/client_form.html", context)
