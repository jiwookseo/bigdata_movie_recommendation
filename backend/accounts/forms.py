from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["username", "is_staff", "age", "occupation", "gender"]


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ["age", "occupation", "gender"]