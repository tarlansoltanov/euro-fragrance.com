from django.views.generic import DetailView

from server.apps.category.models import Category


class CategoryView(DetailView):
    """Category Product List view."""

    model = Category
    context_object_name = "category"

    template_name = "products/shop.html"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.object.name,
            "products": self.object.get_products(),
        }
