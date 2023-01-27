from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required(login_url="account_login")
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
@login_required(login_url="account_login")
def payment_cancelled(request):
    messages.error(
        request, "There was a problem processing your payment. Kindly try again!"
    )
    return render(request, "payments/payment_cancelled.html")
