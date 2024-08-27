from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={"autofocus": True}))

# class ManagerLoginForm(AuthenticationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#
# class TeacherLoginForm(AuthenticationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
