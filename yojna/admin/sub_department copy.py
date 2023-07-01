from django.contrib import admin
from yojna.models import SubdepartmentModel



class SubdepartmentAdmin(admin.ModelAdmin):
    list_max_show_all = 500
    list_per_page = 500
    list_display = ['id', 'name', 'department_id', 'created_at', 'modified_at']
    search_fields = ['name']
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(SubdepartmentModel, SubdepartmentAdmin)
