from django.db import models

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

    class Meta:
        verbose_name = 'Timeslot'
        verbose_name_plural = 'Timeslots'

    def __str__(self):
        return f"{self.schoolclass} - {self.subject} - {self.day_of_week}"
