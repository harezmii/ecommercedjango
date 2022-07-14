from django import forms


class NewsletterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField()


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(max_length=256)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(max_length=256)


class PasswordResetForm(forms.Form):
    password = forms.CharField(max_length=256)
    passwordAgain = forms.CharField(max_length=256)
