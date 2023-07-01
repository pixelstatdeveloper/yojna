from yojna.models import vyaktinsathi
from django.contrib import admin


class vyaktinsathiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(vyaktinsathi,vyaktinsathiAdmin)