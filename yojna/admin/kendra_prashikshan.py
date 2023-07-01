from yojna.models import kendra_prashikshan
from django.contrib import admin


class kendra_prashikshanAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(kendra_prashikshan, kendra_prashikshanAdmin)