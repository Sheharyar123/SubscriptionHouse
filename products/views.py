from paypal.standard.forms import PayPalPaymentsForm
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View, DetailView
from django.conf import settings
from .models import Product, OrderItem
from .forms import ContactForm


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        product_list = Product.objects.filter(active=True)
        context = {"product_list": product_list, "form": ContactForm}
        return render(request, "products/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            name = form.cleaned_data["name"]
            email_from = form.cleaned_data["email"]
            phone_no = form.cleaned_data["phone_no"]
            message = f'{form.cleaned_data["comment"]}\n\n. Sent by {name}.\nPhone No is {phone_no}'
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


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_object(self):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        order_item = OrderItem.objects.create(product=product, user=user, paid=False)
        host = self.request.get_host()
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": order_item.product.price,
            "item_name": order_item.product.title,
            "invoice": str(order_item.id),
            "currency_code": "USD",
            "notify_url": f"http://{host}{reverse('paypal-ipn')}",
            "return_url": f"http://{host}{reverse('payments:payment_completed')}",
            "cancel_return": f"http://{host}{reverse('payments:payment_cancelled')}",
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context["form"] = form
        return context
