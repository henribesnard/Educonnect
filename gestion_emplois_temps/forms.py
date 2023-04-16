from django import forms
from .models import Timeslot

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['schoolclass', 'course', 'start_hour', 'end_hour', 'day_of_week']
