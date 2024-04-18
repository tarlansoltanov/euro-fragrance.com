from django.urls import path

from server.apps.product.views import ProductDetailView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="detail"),
]
