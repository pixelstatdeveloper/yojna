from yojna.models import shahu_fule
from django.contrib import admin


class shahu_fuleAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(shahu_fule,shahu_fuleAdmin)