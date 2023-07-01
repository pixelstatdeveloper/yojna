from django.contrib import admin

from yojna.models import SchemeRegistrationMediaModel


class SchemeRegistrationMediaAdmin(admin.ModelAdmin):
    list_max_show_all = 500
    list_per_page = 500

    list_display = ['id', 'scheme_registration', 'category', 'arza', 'file_path', 'created_at', 'modified_at']

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(SchemeRegistrationMediaModel, SchemeRegistrationMediaAdmin)
