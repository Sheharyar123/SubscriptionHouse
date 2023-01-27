from django import forms

from allauth.account.forms import (
    LoginForm,
    SignupForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget = forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control mb-4",
                "placeholder": "Enter your email...",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-4", "placeholder": "••••••••"}
        )


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=255, label="Full Name")
    phone_no = forms.CharField(max_length=50, label="Phone No")

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget = forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control mb-4",
                "placeholder": "e.g. user@domain.com",
            }
        )
        self.fields["name"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "e.g. Sheharyar Ahmad",
            }
        )
        self.fields["phone_no"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "e.g. +1 (650) 251-53-21",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-4", "placeholder": "••••••••"}
        )
        self.fields["password1"].label = "Password"
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-4", "placeholder": "••••••••"}
        )
        self.fields["password2"].label = "Confirm Password"

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data["name"]
        user.phone_no = self.cleaned_data["phone_no"]
        user.save()
        return user


# class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     def __init__(self, *args, **kwargs):
#         super(CustomSignupForm, self).__init__(*args, **kwargs)
#         self.fields["password1"].widget.attrs.update(
#             {"class": "form-control mb-4", "placeholder": "••••••••"}
#         )
#         self.fields["password2"].widget.attrs.update(
#             {"class": "form-control mb-4", "placeholder": "••••••••"}
#         )
