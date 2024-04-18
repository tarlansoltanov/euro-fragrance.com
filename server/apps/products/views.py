from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from server.apps.base.models import BaseSetting
from server.apps.products.models import Category, Product


class ShopView(ListView):
    """Shop Product List view."""

    model = Product
    queryset = Product.objects.all()
    context_object_name = "products"

    template_name = "products/shop.html"
    paginate_by = 11

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Shop"
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        return context


class ProductView(DetailView):
    """Product view."""

    model = Product
    queryset = Product.objects.all()

    context_object_name = "product"

    template_name = "products/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Product"
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        # Related Products
        context["products"] = (
            Product.objects.filter(categories__in=context["product"].categories.all())
            .exclude(pk=context["product"].pk)
            .distinct()
        )

        return context


class CategoryView(ListView):
    """Category Product List view."""

    model = Product

    context_object_name = "products"

    template_name = "products/shop.html"

    def get_queryset(self):
        """Get Products by Category."""
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])

        return (
            Product.objects.filter(categories__in=self.category.subcategories.all()).distinct()
            if self.category.subcategories.exists()
            else Product.objects.filter(categories__in=[self.category])
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = self.category.name
        context["settings"] = BaseSetting.objects.first()
        context["categories"] = Category.objects.filter(main=None)

        return context
