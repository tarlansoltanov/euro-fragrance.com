from django.contrib import admin

from server.apps.category.models import Category
from server.apps.product.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = (
        "name",
        "category_names",
        "price",
    )

    @admin.display(description="Categories")
    def category_names(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "categories":
            kwargs["queryset"] = Category.objects.filter(main__isnull=False)

        return super().formfield_for_manytomany(db_field, request, **kwargs)
