from django.contrib import admin
from yojna.models import gatai_kamgar

class gatai_kamgarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(gatai_kamgar, gatai_kamgarAdmin)