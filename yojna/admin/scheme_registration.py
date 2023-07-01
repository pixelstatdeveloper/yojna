# from django.contrib import admin

# from yojna.models import SchemeRegistrationModel


# class SchemeRegistrationAdmin(admin.ModelAdmin):
#     list_max_show_all = 500
#     list_per_page = 500

#     list_display = ['id', 'user', 'scheme', 'created_at', 'modified_at']
#     search_fields = ['scheme__name']

#     def has_add_permission(self, request):
#         return True

#     def has_change_permission(self, request, obj=None):
#         return True

#     def has_delete_permission(self, request, obj=None):
#         return True
# admin.site.register(SchemeRegistrationModel, SchemeRegistrationAdmin)
from django.contrib import admin
from yojna.models import SchemeRegistrationModel


class SchemeRegistrationAdmin(admin.ModelAdmin):
    list_max_show_all = 500
    list_per_page = 500

    list_display = ['id', 'user', 'scheme', 'created_at', 'modified_at','application_id']
    search_fields = ['scheme__name']

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(SchemeRegistrationModel, SchemeRegistrationAdmin)