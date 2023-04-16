from django.db import models

from gestion_classes.models import Course
from django.conf import settings

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField('Date')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'roles': 'STUDENT'}, verbose_name='Student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
        ('EXCUSED', 'Excused'),
    ]
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='PRESENT')
    remarks = models.TextField('Remarks', blank=True, null=True)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"
