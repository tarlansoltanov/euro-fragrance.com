from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view."""

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Home"

        return context


class AboutView(TemplateView):
    """About view."""

    template_name = "base/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "About"

        return context


class ContactView(TemplateView):
    """Contact view."""

    template_name = "base/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contact"

        return context
