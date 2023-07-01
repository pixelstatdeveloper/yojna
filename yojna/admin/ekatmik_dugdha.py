from yojna.models import ekatmik_dugdha
from django.contrib import admin


class ekatmik_dugdhaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(ekatmik_dugdha, ekatmik_dugdhaAdmin)