
from yojna.models.user import User_documents
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from yojna.models import UserModel
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(UserAdmin):
    list_max_show_all = 500
    list_per_page = 500

    add_form = UserCreationForm
    form = UserChangeForm
    model = UserModel
    list_display = ('name', 'email', 'mobile_number', 'adhaar_no','profile_pic', 'caste','bpl','bpl_dharak','Gender','is_active', 'is_superuser', 'created_at', 'modified_at','role','department','subdepartment')
    list_filter = ('is_active', 'is_superuser','role','department')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'mobile_number', 'adhaar_no', 'caste','bpl','bpl_dharak','Gender','address','country','state','city','role','department','subdepartment','profile_pic','password')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'email', 'mobile_number', 'adhaar_no', 'caste','bpl','bpl_dharak','role','department','subdepartment','Gender','address','country','state','city','password1', 'password2', 'is_active', 'is_superuser', 'groups',
                'user_permissions')}
         ),
    )
    search_fields = ('name', 'email', 'mobile_number','adhaar_no','profile_pic')
    ordering = ('name',)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(UserModel, UserAdmin)
admin.site.register(User_documents)