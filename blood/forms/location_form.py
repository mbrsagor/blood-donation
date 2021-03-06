from django import forms
from django.forms import TextInput, Select, CheckboxInput

from blood.models.location import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'parent': Select(attrs={'class': 'form-control'}),
            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'location_activity'})
        }
