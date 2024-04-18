from django.db import models

from server.apps.product.logic.querysets import ProductQuerySet


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=255)
    categories = models.ManyToManyField("category.Category", related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()

    objects = ProductQuerySet.as_manager()

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    @property
    def image(self):
        return self.images.first().image if self.images.exists() else None

    @property
    def get_categories(self):
        return ", ".join([c.name for c in self.categories.all()])

    @property
    def related_products(self):
        return Product.objects.filter_by_category(self.categories.all()).exclude(id=self.id).distinct()


class ProductImage(models.Model):
    """Model definition for ProductImage."""

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products")

    class Meta:
        """Meta definition for ProductImage."""

        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        """Unicode representation of ProductImage."""
        return f"{self.product.name} - {self.image.name}"
