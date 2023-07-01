from yojna.models import shaskiy_ashramshala
from django.contrib import admin


class shaskiy_ashramshalaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(shaskiy_ashramshala, shaskiy_ashramshalaAdmin)