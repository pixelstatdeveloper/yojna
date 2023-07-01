from yojna.models import shubhmangal_nondni
from django.contrib import admin


class shubhmangal_nondniAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(shubhmangal_nondni, shubhmangal_nondniAdmin)