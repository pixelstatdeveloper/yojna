from yojna.models import magas_shilai
from django.contrib import admin


class magas_shilaiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(magas_shilai, magas_shilaiAdmin)