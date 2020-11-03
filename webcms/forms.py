from django import forms
from .models import ContactUs

class ContactModel(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'message'
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name