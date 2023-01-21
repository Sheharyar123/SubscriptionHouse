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

        if order_item.product.price == ipn.mc_gross:
            # mark the order as paid
            order_item.paid = True
            order_item.save()
            subject = "Welcome to Subscription House."
            # user = order_item.user
            # message = f"Hi {user.name}. You have successfully subscribed to {order_item.product.title} till {}"
