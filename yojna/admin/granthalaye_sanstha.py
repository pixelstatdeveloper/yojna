from yojna.models import sanstha_sabhasad
from django.contrib import admin


class sanstha_sabhasadAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(sanstha_sabhasad,sanstha_sabhasadAdmin)