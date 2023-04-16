from django import forms
from .models import Establishment, EstablishmentType

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ('name', 'address', 'types', 'category', 'phone_number', 'head')

class EstablishmentTypeForm(forms.ModelForm):
    class Meta:
        model = EstablishmentType
        fields = ('name',)
