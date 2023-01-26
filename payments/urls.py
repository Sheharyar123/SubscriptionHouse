from django.urls import path

from .views import payment_completed, payment_cancelled

app_name = "payments"

urlpatterns = [
    path("payment-completed/", payment_completed, name="payment_completed"),
    path("payment-cancelled/", payment_cancelled, name="payment_cancelled"),
]
