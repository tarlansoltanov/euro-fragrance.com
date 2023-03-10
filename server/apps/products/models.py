from django.db import models


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(verbose_name="Name", max_length=255)
    categories = models.ManyToManyField("Category", verbose_name="Categories", related_name="products")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
    
    @property
    def image(self):
        if self.images.exists():
            return self.images.first().image
    

class ProductImage(models.Model):
    """Model definition for ProductImage."""

    product = models.ForeignKey("Product", verbose_name="Product", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", upload_to="products")

    class Meta:
        """Meta definition for ProductImage."""

        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        """Unicode representation of ProductImage."""
        return f"{self.product.name} - {self.image.name}"
    
    @property
    def url(self):
        return self.image.url


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(verbose_name="Name", max_length=255)
    main = models.ForeignKey("self", verbose_name="Main", related_name="subcategories", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name