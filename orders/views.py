from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from products.models import Product
from .models import Order
from .forms import CheckoutForm
from .utils import generate_order_number


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        form = CheckoutForm
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        context = {"form": form, "product": product}
        return render(request, "orders/checkout.html", context)

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        if form.is_valid():
            order = Order()
            order.first_name = form.cleaned_data["first_name"]
            order.last_name = form.cleaned_data["last_name"]
            order.phone_no = form.cleaned_data["phone_no"]
            order.email = request.user.email
            order.total = product.price
            order.save()
            order.order_number = generate_order_number(order.id)
            order.save()
            messages.success(request, "Your form was submitted successfully!")
            return redirect(product.get_absolute_url())
        else:
            context = {"form": form}
            return render(request, "orders/checkout.html", context)
