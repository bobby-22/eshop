from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is unavailable")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This e-mail is unavailable")
        return email
    
    def clean(self):
        form_data = self.cleaned_data
        if form_data.get("password1") != form_data.get("password2"):
            self.add_error('password1', "Passwords didn't match")
        return form_data
