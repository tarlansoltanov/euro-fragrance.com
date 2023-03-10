from django.urls import path
from . import views

app_name = 'server.apps.products'

urlpatterns = [
    path('', views.shop, name='shop'),
]