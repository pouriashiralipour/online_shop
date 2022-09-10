from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )
        fields = ('username', 'email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', )


class YourSignupForm(SignupForm):
    field_order = ['email', 'username', 'password1', 'password2']