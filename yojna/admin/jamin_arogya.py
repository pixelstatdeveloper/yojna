from yojna.models import aarogya_patrika
from django.contrib import admin


class aarogya_patrikaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(aarogya_patrika,aarogya_patrikaAdmin)