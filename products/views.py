from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Product, OrderItem


class ProductListView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(active=True)


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
        order_item = OrderItem.objects.create(product=product, paid=False)
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
