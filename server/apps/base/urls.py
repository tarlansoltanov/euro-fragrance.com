from django.urls import path
from . import views

app_name = 'server.apps.base'

urlpatterns = [
    path('', views.home, name='home'),
]