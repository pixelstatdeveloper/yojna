from yojna.models import pravinya_rajya
from django.contrib import admin


class pravinya_rajyaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(pravinya_rajya,pravinya_rajyaAdmin)