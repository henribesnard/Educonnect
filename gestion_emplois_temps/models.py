from django.db import models
from django.conf import settings
from gestion_classes.models import Schoolclass, Course


class Timeslot(models.Model):
    id = models.AutoField(primary_key=True)
    schoolclass = models.ForeignKey(Schoolclass, on_delete=models.CASCADE, verbose_name='schoolclass')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='subject', blank=True, null=True)
    start_hour = models.TimeField('Heure de début')
    end_hour = models.TimeField('Heure de fin')
    DAY_CHOICES = [
        ('LUNDI', 'Lundi'),
        ('MARDI', 'Mardi'),
        ('MERCREDI', 'Mercredi'),
        ('JEUDI', 'Jeudi'),
        ('VENDREDI', 'Vendredi'),
        ('SAMEDI', 'Samedi'),
    ]
    day_of_week = models.CharField('Jour de la semaine', max_length=15, choices=DAY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_timeslots', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a créé')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_timeslots', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a mis à jour')

    class Meta:
        verbose_name = 'Timeslot'
        verbose_name_plural = 'Timeslots'

    def __str__(self):
        return f"{self.schoolclass} -{self.course}- {self.day_of_week}-{self.start_hour} - {self.end_hour} "
