from django.urls import path

from server.apps.products.views import CategoryView, ProductView, ShopView

app_name = "products"

urlpatterns = [
    path("", ShopView.as_view(), name="shop"),
    path("product/<int:pk>/", ProductView.as_view(), name="product"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
]
