from yojna.models import divyadivyang_anudan
from django.contrib import admin


class divyadivyang_anudanAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(divyadivyang_anudan, divyadivyang_anudanAdmin)