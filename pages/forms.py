from django.shortcuts import forms
from .models import ContactForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        exclude = ['phone_number']


class ContactAboutPageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        exclude = ['subject']