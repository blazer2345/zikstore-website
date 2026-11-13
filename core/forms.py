from django import forms
from .models import Users

# signup form
class SignupForm(forms.Form):
  username = forms.CharField(label="username", widget=forms.TextInput(
      attrs={"placeholder": "enter your username", "class": "form-control"}
  ))

  def clean_username(self):
    return self.cleaned_data['username'].title()

  email = forms.EmailField(label="user email", widget=forms.EmailInput(
    attrs={"placeholder": "enter Email address", "class": "form-control"}
  ))

  def clean_email(self):
      email = self.cleaned_data['email'].strip().lower()

      if Users.objects.filter(email=email).exists():
         raise forms.ValidationError("this email is already registered")
      return email
      
  phone = forms.CharField(max_length=15, label="phone number")

  password = forms.CharField(label="password", widget=forms.PasswordInput(
     attrs={"placeholder": "enter your password"}
  ))
  def clean_password(self):
      password = self.cleaned_data['password'].title()

      if len(password) < 8:
         raise forms.ValidationError(
            "password must contains atleast 8 characters."
         )
      return password


class LoginForm(forms.Form):
   email = forms.EmailField(label="user email", widget=forms.EmailInput(
    attrs={"placeholder": "enter Email address", "class": "form-control"}
  ))  

   password = forms.CharField(label="password", widget=forms.PasswordInput(
        attrs={"placeholder": "enter your password"}
     ))
   def clean_password(self):
         password = self.cleaned_data['password'].title()
   
         if len(password) < 8:
            raise forms.ValidationError(
               "password must contains atleast 8 characters."
            )
         return password