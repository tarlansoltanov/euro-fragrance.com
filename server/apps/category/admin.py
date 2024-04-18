from django.contrib import admin

from server.apps.category.models import Category


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
