import stripe
from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def process_stripe_payments(request):
    order_item = request.user.order_items.first()
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("payments:payment_completed"))
        cancel_url = request.build_absolute_uri(reverse("payments:payment_cancelled"))
        # Stripe checkout session data
        session_data = {
            "mode": "payment",
            "client_reference_id": order_item.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }
        session_data["line_items"].append(
            {
                "price_data": {
                    "unit_amount": int(order_item.product.price * Decimal("100")),
                    "currency": "usd",
                    "product_data": {
                        "name": order_item.product.title,
                    },
                },
                "quantity": 1,
            },
        )
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)
        # redirect to Stripe payment form
        return redirect(session.url, code=303)
    else:
        return render(request, "payments/process_payment.html", locals())


@csrf_exempt
def payment_completed(request):
    user = request.user
    order_item = user.order_items.last()
    if order_item.product.title.title() != "Get Hired":
        messages.success(
            request,
            "Your payment was processed successfully. Your Coupon is being generated. Our customer care agent will contact you in 1 hour with your coupon.",
        )
    else:
        messages.success(
            request,
            "Your payment was processed successfully. Our customer care agent will contact you in 1 hour for further discussion.",
        )
    return render(request, "payments/payment_completed.html")


@csrf_exempt
def payment_cancelled(request):
    messages.error(
        request, "There was a problem processing your payment. Kindly try again!"
    )
    return render(request, "payments/payment_cancelled.html")
