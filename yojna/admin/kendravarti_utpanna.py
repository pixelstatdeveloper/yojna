from yojna.models import kendravarti_utpanna
from django.contrib import admin


class kendravarti_utpannaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(kendravarti_utpanna, kendravarti_utpannaAdmin)