from yojna.models import samuhik_vivah
from django.contrib import admin


class samuhik_vivahAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(samuhik_vivah, samuhik_vivahAdmin)