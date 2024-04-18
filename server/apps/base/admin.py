from django.contrib import admin

from server.apps.base.models import BaseSetting


@admin.register(BaseSetting)
class BaseSettingAdmin(admin.ModelAdmin):
    list_display = ("company_name", "email", "phone")

    def has_add_permission(self, request):
        return not self.model.objects.count()

    def has_delete_permission(self, request, obj=None):
        return False
