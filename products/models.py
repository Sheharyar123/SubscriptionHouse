from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
import uuid

User = get_user_model()


class Product(models.Model):
    PLAN_TYPE = (
        ("BASIC", "BASIC"),
        ("POPULAR", "POPULAR"),
        ("ENTERPRISE", "ENTERPRISE"),
    )
    BACKGROUND_TYPE = (
        ("primary", "primary"),
        ("secondry", "secondry"),
        ("danger", "danger"),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    background_type = models.CharField(choices=BACKGROUND_TYPE, max_length=30)
    plan_type = models.CharField(choices=PLAN_TYPE, max_length=30)
    price = models.IntegerField()
    title = models.CharField(max_length=50)
    description = RichTextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan_type


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    # paid
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} bought {self.product.title}"
