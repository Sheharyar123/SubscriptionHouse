from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("subscriptions-house-admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("products.urls")),
    path("", include("orders.urls")),
    path("paypal/", include("paypal.standard.ipn.urls")),
    path("payments/", include("payments.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
