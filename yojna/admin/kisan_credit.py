from yojna.models import kisan_credit
from django.contrib import admin


class kisan_creditAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(kisan_credit, kisan_creditAdmin)