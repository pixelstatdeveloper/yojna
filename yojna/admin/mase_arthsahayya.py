from yojna.models import masemari_arth
from django.contrib import admin


class masemari_arthAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(masemari_arth,masemari_arthAdmin)