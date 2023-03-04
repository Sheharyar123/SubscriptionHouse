from django.urls import path
from .views import CheckoutView

app_name = "orders"

urlpatterns = [
    path("checkout/<uuid:pk>/", CheckoutView.as_view(), name="checkout"),
]
