from yojna.models import polis_bhartipurva
from django.contrib import admin


class polis_bhartipurvaAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(polis_bhartipurva,polis_bhartipurvaAdmin)