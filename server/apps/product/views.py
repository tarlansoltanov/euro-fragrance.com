from django.views.generic import DetailView, ListView

from server.apps.product.models import Product


class ProductListView(ListView):
    """Product List view."""

    model = Product
    context_object_name = "products"

    paginate_by = 11

    template_name = "products/shop.html"

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(**kwargs), "title": "Shop"}


class ProductDetailView(DetailView):
    """Product Detail view."""

    model = Product
    context_object_name = "product"

    template_name = "products/product.html"

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(**kwargs), "title": self.object.name}
