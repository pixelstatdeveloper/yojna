from yojna.models import thakkar
from django.contrib import admin


class ThakkarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(thakkar,ThakkarAdmin)