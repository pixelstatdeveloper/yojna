from yojna.models import shubh_vivah
from django.contrib import admin


class shubh_vivahAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(shubh_vivah,shubh_vivahAdmin)