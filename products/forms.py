from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Name", "class": "form-control"}),
    )
    email = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
    )
    phone_no = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Phone No", "class": "form-control"}
        ),
    )
    subject = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Subject", "class": "form-control"}
        ),
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Comment", "class": "form-control"}
        ),
    )
