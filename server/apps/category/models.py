from django.db import models

from server.apps.product.models import Product


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=255)
    main = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    def get_products(self):
        """Return all products in this category and its children."""
        return Product.objects.filter(categories__in=[self] + list(self.children.all())).distinct()
