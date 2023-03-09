from django.contrib import admin
from django.forms import ValidationError
from .models import Product, ProductImage, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'categories')

    def categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    
    categories.short_description = "Categories"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main')

    def main(self, obj):
        return obj.main.name if obj.main else None
