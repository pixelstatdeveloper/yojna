from yojna.models import upajivikesathi
from django.contrib import admin


class upajivikesathiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(upajivikesathi,upajivikesathiAdmin)