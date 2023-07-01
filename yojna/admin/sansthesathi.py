from yojna.models import bharat_sanstha
from django.contrib import admin


class bharat_sansthaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(bharat_sanstha,bharat_sansthaAdmin)