from django.contrib import admin

from server.apps.products.models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category_names")

    inlines = [ProductImageInline]

    @admin.display(description="Categories")
    def category_names(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "categories":
            kwargs["queryset"] = Category.objects.filter(main__isnull=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "main")

    def main(self, obj):
        return obj.main.name if obj.main else None

    main.short_description = "Main"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main":
            kwargs["queryset"] = Category.objects.filter(main=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
