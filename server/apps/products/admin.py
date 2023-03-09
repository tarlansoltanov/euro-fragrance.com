from django.contrib import admin
from django.forms import ValidationError
from .models import Product, ProductImage, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'categories')

    inlines = [ProductImageInline]

    def categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    
    categories.short_description = "Categories"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main')

    def main(self, obj):
        return obj.main.name if obj.main else None
    
    main.short_description = "Main"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main":
            kwargs["queryset"] = Category.objects.filter(main=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)