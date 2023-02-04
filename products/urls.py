from django.urls import path
from .views import HomePageView, ProductListView, ProductDetailView

app_name = "products"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("product/<uuid:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
