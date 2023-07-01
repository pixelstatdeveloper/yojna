from django.contrib import admin
from yojna.models import anusuchit_50takke

class anusuchit_50takkeAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(anusuchit_50takke, anusuchit_50takkeAdmin)