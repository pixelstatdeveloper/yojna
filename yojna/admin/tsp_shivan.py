from yojna.models import tsp_shivnyantra
from django.contrib import admin


class tsp_shivnyantraAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(tsp_shivnyantra,tsp_shivnyantraAdmin)