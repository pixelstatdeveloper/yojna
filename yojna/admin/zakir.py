from yojna.models import zakir_hus
from django.contrib import admin


class zakir_husAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(zakir_hus,zakir_husAdmin)