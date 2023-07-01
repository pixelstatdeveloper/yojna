from yojna.models import mahatmagandhi_reshim
from django.contrib import admin


class mahatmagandhi_reshimAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(mahatmagandhi_reshim, mahatmagandhi_reshimAdmin)