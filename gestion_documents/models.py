from django.db import models

from django.conf import settings
from gestion_classes.models import Course

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description', blank=True, null=True)
    file = models.FileField('File', upload_to='documents/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', blank=True, null=True)
    VISIBILITY_CHOICES = [
        ('TEACHERS', 'Teachers'),
        ('STUDENTS', 'Students'),
        ('PARENTS', 'Parents'),
        ('ALL', 'All'),
    ]
    visibility = models.CharField('Visibility', max_length=15, choices=VISIBILITY_CHOICES, default='ALL')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
