from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from yojna.models import UserModel


class UserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('name', 'email', 'mobile_number', 'is_superuser')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('name', 'email', 'mobile_number', 'is_superuser')
