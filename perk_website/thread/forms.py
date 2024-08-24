from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Specify the model to use
        fields = ['fname', 'lname', 'email', 'message']