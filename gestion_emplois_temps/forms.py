from django import forms
from .models import Timeslot, Room
from gestion_classes.models import Course, Schoolclass

class TimeslotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.establishment = kwargs.pop('establishment', None)
        super(TimeslotForm, self).__init__(*args, **kwargs)
        if self.establishment:
            self.fields['schoolclass'].queryset = Schoolclass.objects.filter(establishment=self.establishment)
            self.fields['course'].queryset = Course.objects.filter(establishment=self.establishment)
            self.fields['room'].queryset = Room.objects.filter(establishment=self.establishment)

    class Meta:
        model = Timeslot
        fields = ['schoolclass', 'course', 'room', 'start_datetime', 'end_datetime']

