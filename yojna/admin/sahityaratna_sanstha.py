from yojna.models import lokshahir_sanstha
from django.contrib import admin


class lokshahir_sansthaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(lokshahir_sanstha,lokshahir_sansthaAdmin)