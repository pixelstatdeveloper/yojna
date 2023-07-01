from yojna.models import pramod_mah
from django.contrib import admin


class pramod_mahAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(pramod_mah,pramod_mahAdmin)