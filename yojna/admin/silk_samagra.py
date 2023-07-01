from yojna.models import silk_samagra
from django.contrib import admin


class silk_samagraAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(silk_samagra, silk_samagraAdmin)