from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class PostForm(forms.Form):
    body_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 82, 'placeholder': 'Tell me something... ',
                                     'onkeypress': 'counter(this)', 'onkeyup': 'counter(this)',
                                     'onchange': 'counter(this)'}), max_length=140, label='')

    def clean(self):
        if self.cleaned_data.get('body_text') == '':
            raise ValidationError('Post is empty!')
        return self.cleaned_data


class LoginForm(forms.Form):
    user_login = forms.CharField(label="your login")
    user_password = forms.CharField(widget=forms.PasswordInput, label="password", min_length=6, max_length=30)

    def clean(self):
        name = self.cleaned_data.get('user_login')
        if not User.objects.filter(username=name):
            raise ValidationError('Wrong user!')
        return self.cleaned_data


class RegisterForm(forms.Form):
    user_email = forms.EmailField(label="Email")
    user_password = forms.CharField(widget=forms.PasswordInput, label="password", min_length=6, max_length=30)
    retype_user_password = forms.CharField(widget=forms.PasswordInput, label="re-type password", min_length=6,
                                           max_length=30)
    user_firstname = forms.CharField(label="Your 1st name")
    user_lastname = forms.CharField(label="Your last name")

    def clean(self):
        pwd = self.cleaned_data.get('user_password')
        pwd2 = self.cleaned_data.get('retype_user_password')
        if not pwd == pwd2:
            raise ValidationError('Passwords mismatch!')

        try:
            user = User.objects.get(username=self.cleaned_data.get('user_email'))
            raise forms.ValidationError('This email is used.')
        except:
            pass

        return self.cleaned_data
