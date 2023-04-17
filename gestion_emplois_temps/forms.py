from django import forms
from .models import Timeslot, Room

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ('schoolclass', 'course', 'room', 'start_datetime', 'end_datetime')

    def __init__(self, *args, schoolclass=None, **kwargs):
        super().__init__(*args, **kwargs)
        if schoolclass:
            self.fields['room'].queryset = Room.objects.filter(establishment=schoolclass.establishment)

    def get_available_rooms(self, start_datetime, end_datetime, schoolclass):
        """
        Retourne les salles disponibles pour les dates et heures de début et de fin données
        et l'établissement de la classe.
        """
        return Room.objects.filter(
            establishment=schoolclass.establishment
        ).exclude(
            timeslot__start_datetime__lt=end_datetime,
            timeslot__end_datetime__gt=start_datetime
        )
