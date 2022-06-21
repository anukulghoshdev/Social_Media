from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #UserCreationForm-> username', 'password1', 'password2',| AuthenticationForm-> username, password
from django.contrib.auth.models import User # 'username', 'password', 'email', 'first_name', 'last_name'

from App_RegLog.models import UserProfile
#UserCreationForm-> sign up form, AuthenticationForm-> log in form

class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    username =forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')



class UserProfileEditForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ('user', )
