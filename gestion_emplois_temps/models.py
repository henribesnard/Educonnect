from django.db import models
from django.conf import settings
from gestion_classes.models import Schoolclass, Course
from etablissements.models import Establishment

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nom', max_length=100)
    capacity = models.IntegerField('Capacité', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, verbose_name='Établissement')

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name

class Timeslot(models.Model):
    id = models.AutoField(primary_key=True)
    schoolclass = models.ForeignKey(Schoolclass, on_delete=models.CASCADE, verbose_name='schoolclass')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='subject', blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='room', blank=True, null=True)
    start_datetime = models.DateTimeField('Date et heure de début')
    end_datetime = models.DateTimeField('Date et heure de fin')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_timeslots', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a créé')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_timeslots', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a mis à jour')

    class Meta:
        verbose_name = 'Timeslot'
        verbose_name_plural = 'Timeslots'
    
    def has_overlapping(self):
        overlapping_timeslots = Timeslot.objects.filter(
            course=self.course,
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime,
        ).exclude(pk=self.pk)
        
        return overlapping_timeslots.exists()

    def __str__(self):
        return f"{self.schoolclass} - {self.course} - {self.room} - {self.start_datetime} - {self.end_datetime}"




