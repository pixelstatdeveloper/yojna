from yojna.models import magasvargiy_mula
from django.contrib import admin


class magasvargiy_mulaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(magasvargiy_mula,magasvargiy_mulaAdmin)