from yojna.models import bhumihin_daridrya
from django.contrib import admin


class bhumihin_daridryaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(bhumihin_daridrya, bhumihin_daridryaAdmin)