from django.contrib import admin
from .models import Product, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "plan_type",
        "background_type",
        "price",
        "active",
        "is_featured",
    ]
    list_editable = [
        "active",
        "is_featured",
    ]
    list_filter = ["plan_type", "price"]
    search_fields = ["plan_type", "title", "price"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "customer_name",
        "customer_email",
        "customer_phoneNo",
        "product",
        "created_on",
        "paid",
    ]
    readonly_fields = [
        "paid",
        "created_on",
    ]
