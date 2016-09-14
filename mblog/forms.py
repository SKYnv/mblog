from django import forms
from django.contrib.auth import login
from django.views.generic.edit import FormView


class PostForm(forms.Form):
    body_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 82, 'placeholder': 'Tell me something... ',
                                     'onkeypress': 'counter(this)', 'onkeyup': 'counter(this)',
                                     'onchange': 'counter(this)'}), max_length=140, label='')


class LoginForm(forms.Form):
    user_login = forms.CharField(label="your login")
    user_password = forms.CharField(widget=forms.PasswordInput, label="password", min_length=6, max_length=30)

