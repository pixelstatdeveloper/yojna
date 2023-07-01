from yojna.models import mada_shivnyantra
from django.contrib import admin


class mada_shivnyantraAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(mada_shivnyantra,mada_shivnyantraAdmin)