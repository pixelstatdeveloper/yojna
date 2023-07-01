from yojna.models import sankalp_skill
from django.contrib import admin


class sankalp_skillAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(sankalp_skill,sankalp_skillAdmin)