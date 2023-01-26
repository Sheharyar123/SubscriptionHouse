from ckeditor.fields import RichTextField
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import uuid

from django.urls import reverse

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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.CharField(max_length=50)
    description = RichTextField()
    active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on", "-added_on"]

    def __str__(self):
        return f"{self.plan_type} - {self.title}"

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"pk": self.pk})


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    paid = models.BooleanField(default=False)
    created_on = models.DateField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        ordering = ["-updated_on", "-created_on"]

    @property
    def valid_till(self):
        if self.product.is_featured:
            valid_date = self.created_on + timedelta(days=180)
        else:
            valid_date = self.created_on + timedelta(days=30)
        return valid_date

    @property
    def customer_name(self):
        return self.user.name

    @property
    def customer_email(self):
        return self.user.email

    @property
    def customer_phoneNo(self):
        return self.user.phone_no
