from django.contrib import admin
from yojna.models import divyang_xerox

class divyang_xeroxAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(divyang_xerox, divyang_xeroxAdmin)