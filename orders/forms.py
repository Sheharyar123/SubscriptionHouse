from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_no",
        ]

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget = forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control mb-4",
                "placeholder": "e.g. user@domain.com",
            }
        )
        self.fields["first_name"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "e.g. John",
            }
        )
        self.fields["last_name"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "e.g. Doe",
            }
        )
        self.fields["phone_no"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "e.g. +1 (650) 251-53-21",
            }
        )
