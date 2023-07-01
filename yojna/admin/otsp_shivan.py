from yojna.models import otsp_shivnyantra
from django.contrib import admin


class otsp_shivnyantraAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(otsp_shivnyantra,otsp_shivnyantraAdmin)