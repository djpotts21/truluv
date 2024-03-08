# truluv/forms.py

from allauth.account.forms import LoginForm
from . import forms
from django import forms

# All Auth Login Form
class TruLuvLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(TruLuvLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'email@example.com'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})