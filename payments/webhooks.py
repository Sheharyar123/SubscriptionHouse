import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import OrderItem


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event.type == "checkout.session.completed":
        session = event.data.object
        subject = "Welcome to Subscription House."
        email_from = settings.EMAIL_HOST_USER

        if session.mode == "payment" and session.payment_status == "paid":
            try:
                order_item = OrderItem.objects.get(id=session.client_reference_id)
            except OrderItem.DoesNotExist:
                return HttpResponse(status=404)
            # mark order as paid
            order_item.paid = True
            order_item.save()
            recipient_list = [
                order_item.user.email,
            ]
            if order_item.product.title.title() != "Get Hired":
                message = f"""Hi {order_item.user.name}. You have successfully subscribed to "{order_item.product.plan_type} - {order_item.product.title}" till {order_item.valid_till}.\nYour Coupon is being generated. Our customer care agent will contact you in 1 hour with your coupon."""
            else:
                message = f"""Hi {order_item.user.name}. You have successfully subscribed to "{order_item.product.plan_type} - {order_item.product.title}" till {order_item.valid_till}.\nOur customer care agent will contact you in 1 hour for further discussion."""

            send_mail(
                subject,
                message,
                email_from,
                recipient_list,
                fail_silently=False,
            )
        else:
            message = f"""Hi {order_item.user.name}.\nSorry there was a problem processing your payment.
                   Kindly try again!!"""
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return HttpResponse(status=200)
