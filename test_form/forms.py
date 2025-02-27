from django import forms
from .models import UserFormModel

class UserForm(forms.ModelForm):

    class Meta:
        model = UserFormModel
        fields = '__all__'