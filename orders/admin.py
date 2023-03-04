from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_no",
    ]
    ordering = ["-updated_on", "-created_on"]


admin.site.register(Order, OrderAdmin)
