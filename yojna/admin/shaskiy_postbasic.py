from yojna.models import shaskiy_postbasic
from django.contrib import admin


class shaskiy_postbasicAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(shaskiy_postbasic, shaskiy_postbasicAdmin)