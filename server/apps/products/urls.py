from django.urls import path
from . import views

app_name = 'server.apps.products'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<int:pk>/', views.category, name='category'),
]