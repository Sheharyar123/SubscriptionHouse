from django.urls import path
from .views import HomePageView, ProductListView, ProductDetailView, ClientFormView

app_name = "products"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("client_form/", ClientFormView.as_view(), name="client_form"),
    path("product/<uuid:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
