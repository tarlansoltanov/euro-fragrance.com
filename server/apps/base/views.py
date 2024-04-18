from django.views.generic import TemplateView

from server.apps.base.models import BaseSetting
from server.apps.products.models import Category


class HomeView(TemplateView):
    """Home view."""

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Home"
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        return context


class AboutView(TemplateView):
    """About view."""

    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "About"
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        return context


class ContactView(TemplateView):
    """Contact view."""

    template_name = "base/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact"
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        return context
