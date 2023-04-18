from django import forms
from .models import Timeslot

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['schoolclass', 'course', 'room', 'start_datetime', 'end_datetime']
