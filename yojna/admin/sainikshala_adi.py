from yojna.models import sainikshala_adi
from django.contrib import admin


class sainikshala_adiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(sainikshala_adi, sainikshala_adiAdmin)