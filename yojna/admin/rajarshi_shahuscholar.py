from yojna.models import rajarshi_shahuscholar
from django.contrib import admin


class rajarshi_shahuscholarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(rajarshi_shahuscholar, rajarshi_shahuscholarAdmin)