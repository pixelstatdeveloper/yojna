from yojna.models import otsp_cycl
from django.contrib import admin


class otsp_cyclAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(otsp_cycl,otsp_cyclAdmin)