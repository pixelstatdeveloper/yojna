from yojna.models import punyshlok_ahilya
from django.contrib import admin


class punyshlok_ahilyaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(punyshlok_ahilya,punyshlok_ahilyaAdmin)