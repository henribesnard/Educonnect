from django.db import models
from django.conf import settings

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Sender')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages', verbose_name='Recipient')
    subject = models.CharField('Subject', max_length=200)
    content = models.TextField('Content')
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.sender} - {self.recipient} - {self.subject}"


class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author')
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)
    schoolclass = models.ForeignKey('gestion_classes.Schoolclass', on_delete=models.CASCADE, verbose_name='School Class', blank=True, null=True)

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.title
