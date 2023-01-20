from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment_completed(request):
    return render(request, "payments/payment_completed.html")


@csrf_exempt
def payment_cancelled(request):
    return render(request, "payments/payment_cancelled.html")
