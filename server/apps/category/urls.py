from django.urls import path

from server.apps.category.views import CategoryView

app_name = "products"

urlpatterns = [
    path("category/<int:pk>/", CategoryView.as_view(), name="detail"),
]
