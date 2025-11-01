from django import forms

from .models import Boat, Setting

class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        exclude = ['adopter']

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        exclude = ['adopter']
