from yojna.models import hami_yojna
from django.contrib import admin


class hami_yojnaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(hami_yojna,hami_yojnaAdmin)