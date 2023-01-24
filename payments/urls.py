from django.urls import path

from .views import process_stripe_payments, payment_completed, payment_cancelled
from .webhooks import stripe_webhook

app_name = "payments"

urlpatterns = [
    path("process-payment/", process_stripe_payments, name="process_payment"),
    path("payment-completed/", payment_completed, name="payment_completed"),
    path("payment-cancelled/", payment_cancelled, name="payment_cancelled"),
    path("webhook/", stripe_webhook, name="stripe_webhook"),
]
