from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .models import OrderItem
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == "Completed":
        # payment was successful
        order_item = get_object_or_404(OrderItem, id=ipn.invoice)
        subject = "Welcome to Subscription House."
        user = order_item.user
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            user.email,
        ]
        if order_item.product.price == ipn.mc_gross:
            # mark the order as paid
            order_item.paid = True
            order_item.save()
            if order_item.product.title.title() != "Get Hired":
                message = f"""Hi {user.name}. You have successfully subscribed to "{order_item.product.plan_type} - {order_item.product.title}" till {order_item.valid_till}.\nYour Coupon is being generated. Our customer care agent will contact you in 1 hour with your coupon."""
            else:
                message = f"""Hi {user.name}. You have successfully subscribed to "{order_item.product.plan_type} - {order_item.product.title}" till {order_item.valid_till}.\nOur customer care agent will contact you in 1 hour for further discussion."""

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            # Email to owner
            send_mail(
                subject="Email from Subscriptions House",
                message=f"{user.name} has bought the following product.\n'{order_item.product.title} - {order_item.product.plan_type} - ${order_item.product.price}'.\nCustomer's email is {user.email} and phone no is {user.phone_no}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["talha.sharif380@gmail.com"],
                fail_silently=False,
            )

        else:
            message = f"""Hi {user.name}.\nSorry there was a problem processing your payment.
                    Kindly try again!!"""
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    else:
        message = f"""Hi {user.name}.\nSorry there was a problem processing your payment.
                   Kindly try again!!"""
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
