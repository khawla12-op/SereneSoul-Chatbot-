from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

#class for the login
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control main', 'type' : 'text' , 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control main', 'placeholder': 'Password', 'id': 'password'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ("username" , "password")

#class for the register
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control main', 'placeholder': 'Username', 'id': 'username'})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control main', 'placeholder': 'Email', 'id': 'email'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class': 'form-control main', 'placeholder': 'Password', 'id': 'password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control main', 'placeholder': 'Confirm Passord', 'id': ' password'})
    )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "email","password1", "password2"]:
            self.fields[fieldname].help_text = None
                    
    class Meta:
        model = User
        fields = ("username", "email","password1", "password2")