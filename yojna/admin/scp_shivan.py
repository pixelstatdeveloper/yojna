from yojna.models import scp_shivnyantra
from django.contrib import admin


class scp_shivnyantraAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(scp_shivnyantra,scp_shivnyantraAdmin)