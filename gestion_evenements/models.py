from django.db import models

from django.conf import settings

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description', blank=True, null=True)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date', blank=True, null=True)
    location = models.CharField('Location', max_length=255, blank=True, null=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Organizer')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
