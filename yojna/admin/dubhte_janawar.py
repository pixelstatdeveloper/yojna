from yojna.models import dubhte_janawar
from django.contrib import admin


class dubhte_janawarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(dubhte_janawar, dubhte_janawarAdmin)