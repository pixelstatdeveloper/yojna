from yojna.models import din_dayal
from django.contrib import admin


class din_dayalAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(din_dayal,din_dayalAdmin)