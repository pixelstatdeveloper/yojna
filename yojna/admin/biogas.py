from yojna.models import navin_rashtriy
from django.contrib import admin


class navin_rashtriyAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(navin_rashtriy,navin_rashtriyAdmin)