from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')

    def clean_username(self):
        username_or_email = self.cleaned_data.get('username')
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                return user.username
            except User.DoesNotExist:
                pass
        return username_or_email

