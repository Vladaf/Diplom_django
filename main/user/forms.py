from django import forms
from typing import Dict, Any
from django.contrib.auth import authenticate
from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "id": "name",
                "placeholder": "Your Name",
                "data-error": "Please enter your user name",
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "id": "password",
                "placeholder": "Password",
                "data-error": "Please enter your password",
            }
        )
    )

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.cleaned_data["user"] = user
            return self.cleaned_data
        else:
            self.add_error("username", "Invalid username")
            self.add_error("password", "Invalid password")
            raise forms.ValidationError("User not found!")

class RegistrationForm(forms.ModelForm):

    password_repeate = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                    "class": "form-control",
                    "id": "password_repeate",
                    "placeholder": "Repeate password",
                    "data-error": "Please repeate your password",
                }
        )
    )

    class Meta:
        model = User
        #fields = "__all__"
        fields =[
            "username",
            "email",
            "password",
            "is_musician",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "id": "name",
                    "placeholder": "Your Name",
                    "data-error": "Please enter your user name",
                }
            ),
            "email": forms.EmailInput(
                attrs = {
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Email",
                    "data-error": "Please enter your email",
                }
            ),
            "password": forms.PasswordInput(
                attrs = {
                    "class": "form-control",
                    "id": "password",
                    "placeholder": "Password",
                    "data-error": "Please enter your password",
                }
            ),
        }

    def clean(self) -> Dict[str, Any]:
        if self.cleaned_data["password"] != self.cleaned_data["password_repeate"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return super().clean()

    def save(self, commit: bool = False) -> Any:
        user = super().save(commit = commit)
        user.set_password(user.password)
        user.save()
        return user