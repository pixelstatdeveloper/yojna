from yojna.models import swadhar_yoj
from django.contrib import admin


class swadhar_yojAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(swadhar_yoj,swadhar_yojAdmin)