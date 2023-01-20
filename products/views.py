from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(active=True)
