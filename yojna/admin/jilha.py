from yojna.models import jilha_pur
from django.contrib import admin


class jilha_purAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(jilha_pur,jilha_purAdmin)