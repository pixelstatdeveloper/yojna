from yojna.models import dharmik_alp
from django.contrib import admin


class dharmik_alpAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(dharmik_alp,dharmik_alpAdmin)