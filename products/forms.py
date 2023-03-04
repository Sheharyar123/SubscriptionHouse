from django import forms
from .models import Client, JOB_CHOICES, YES_OR_NO
from .validators import allow_only_images


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


class ClientForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your name...", "class": "form-control mb-4"}
        ),
    )
    email = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email...", "class": "form-control mb-4"}
        ),
    )
    phone_no = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your phone no...",
                "class": "form-control mb-4",
            }
        ),
    )

    job_type = forms.CharField(max_length=20, widget=forms.Select(choices=JOB_CHOICES))
    authorized = forms.ChoiceField(choices=YES_OR_NO)
    sponsorship = forms.ChoiceField(choices=YES_OR_NO)
    resume = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control mb-4"}),
        validators=[allow_only_images],
    )

    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "phone_no",
            "address",
            "job_titles",
            "ethnicity",
            "race",
            "location",
            "salary",
            "native_language",
            "nationality",
            "disability",
            "job_type",
            "authorized",
            "sponsorship",
            "disability",
            "resume",
        ]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update(
            {"placeholder": "Enter your address...", "class": "form-control mb-4"}
        )
        self.fields["job_titles"].widget.attrs.update(
            {
                "placeholder": "Enter at least 3 job titles...",
                "class": "form-control mb-4",
            }
        )
        self.fields["ethnicity"].widget.attrs.update(
            {"placeholder": "Enter your ethnicity...", "class": "form-control mb-4"}
        )
        self.fields["race"].widget.attrs.update(
            {"placeholder": "Enter your race...", "class": "form-control mb-4"}
        )
        self.fields["location"].widget.attrs.update(
            {
                "placeholder": "Enter your preferred location...",
                "class": "form-control mb-4",
            }
        )
        self.fields["salary"].widget.attrs.update(
            {
                "placeholder": "Enter your salary requirements...",
                "class": "form-control mb-4",
            }
        )
        self.fields["native_language"].widget.attrs.update(
            {
                "placeholder": "Enter your native language...",
                "class": "form-control mb-4",
            }
        )
        self.fields["nationality"].widget.attrs.update(
            {"placeholder": "Enter your nationality...", "class": "form-control mb-4"}
        )
        self.fields["disability"].widget.attrs.update(
            {"placeholder": "Optional...", "class": "form-control mb-4"}
        )
        self.fields["job_type"].widget.attrs.update({"class": "form-control mb-4"})
        self.fields["authorized"].widget.attrs.update({"class": "form-control mb-4"})
        self.fields["sponsorship"].widget.attrs.update({"class": "form-control mb-4"})
