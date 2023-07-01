from yojna.models import tsp_cycl
from django.contrib import admin


class tsp_cyclAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(tsp_cycl,tsp_cyclAdmin)