from yojna.models import karmavir
from django.contrib import admin


class karmavirAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(karmavir,karmavirAdmin)