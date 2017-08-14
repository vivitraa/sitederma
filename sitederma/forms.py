from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import ListTanya, Kucing


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

class SignupForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firtsname'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastname'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email yang anda masukan sudah terdaftar")
        return email

class PertanyaanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PertanyaanForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget = form.RadioSelect()
            field.empty_value = None
            field.choices = List_Choice
            field.widget.attrs = {'class': 'magic-radio'}

    class Meta:
        model = ListTanya
        fields = '__all__'

class KucingForm(forms.ModelForm):
    nama_kucing = forms.CharField(label='Nama Kucing', widget=forms.TextInput)

    class Meta:
        model = Kucing
        fields = ('nama_kucing', 'umur_kucing', 'gender_kucing')
