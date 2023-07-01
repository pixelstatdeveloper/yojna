from yojna.models import swayamrojgar_divyang
from django.contrib import admin


class swayamrojgar_divyangAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(swayamrojgar_divyang, swayamrojgar_divyangAdmin)