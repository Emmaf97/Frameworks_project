from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Inheritance Relationship
from .models import Profile
import os
from django.conf import settings


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove unwanted fields
        if 'usable_password' in self.fields:
            del self.fields['usable_password']
            
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


def get_image_choices():
    return [
        ('users/images/option1.png', 'Avatar 1'),
        ('users/images/option2.png', 'Avatar 2'),
        ('users/images/option3.png', 'Avatar 3'),
        # Add more as needed
    ]
class ProfileUpdateForm(forms.ModelForm):
    image_choice = forms.ChoiceField(choices=get_image_choices,widget=forms.RadioSelect)
    
    class Meta:
        model = Profile 
        fields = ['image_choice']
        
    def save(self, commit=True):
        profile = super().save(commit=False)
        image_choice = self.cleaned_data.get('image_choice')
        if image_choice:
            profile.image.name = image_choice  # Set the image to the selected predefined one

        if commit:
            profile.save()

        return profile
        
        
        

       