from django.contrib import admin
from yojna.models import andh_vyaktinsathi

class andha_vyaktisathiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(andh_vyaktinsathi, andha_vyaktisathiAdmin)