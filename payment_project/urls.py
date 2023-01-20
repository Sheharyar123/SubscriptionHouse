from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("products.urls")),
    path("paypal/", include("paypal.standard.ipn.urls")),
    path("payments/", include("payments.urls")),
]
