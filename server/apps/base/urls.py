from django.urls import path

from server.apps.base.views import AboutView, ContactView, HomeView

app_name = "base"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
