from django.db import models


class Payment(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id


class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    is_ordered = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
