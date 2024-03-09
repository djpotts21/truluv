# truluv/forms.py

from allauth.account.forms import LoginForm, SignupForm
from django import forms


# All Auth Login Form
class TruLuvLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(TruLuvLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':
                'Username (Your Display Name)'}
            )
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'})


# All Auth Sign Up Form
class TruLuvSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(TruLuvSignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email Address'})
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username (This will be your display name)'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'})
        