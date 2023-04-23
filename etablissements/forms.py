from django import forms
from .models import Establishment, EstablishmentType
from gestion_utilisateurs.models import User

class EstablishmentForm(forms.ModelForm):
    head = forms.ModelChoiceField(
        queryset=User.objects.filter(roles__name__icontains='HEAD'),
        required=False
    )
    
    class Meta:
        model = Establishment
        fields = ['name', 'address', 'types', 'category', 'phone_number', 'head']

class EstablishmentTypeForm(forms.ModelForm):
    class Meta:
        model = EstablishmentType
        fields = ('name',)
