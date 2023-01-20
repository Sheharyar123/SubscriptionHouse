from django.contrib import admin
from .models import Product, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "plan_type", "price", "active"]
    list_editable = [
        "active",
    ]
    list_filter = ["plan_type", "price"]
    search_fields = ["plan_type", "title", "price"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "created_on"]
