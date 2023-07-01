from yojna.models import pra_dhan
from django.contrib import admin


class pra_dhanAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(pra_dhan,pra_dhanAdmin)