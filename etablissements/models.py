from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class EstablishmentType(models.Model):
    NAMES = (
        ('PRESCHOOL', 'Preschool'),
        ('PRIMARY', 'Primary'),
        ('MIDDLE_SCHOOL', 'Middle School'),
        ('HIGH_SCHOOL', 'High School'),
        ('UNIVERSITY', 'University'),
        ('INSTITUTE', 'Institute'),
        ('TRAINING_CENTER', 'Training Center'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=50, choices=NAMES, unique=True)

    class Meta:
        verbose_name = 'Establishment Type'
        verbose_name_plural = 'Establishment Types'

    def __str__(self):
        return self.name


class Establishment(models.Model):
    CATEGORIES = (
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    address = models.TextField('Address')
    types = models.ManyToManyField(EstablishmentType, verbose_name='Types')
    category = models.CharField('Category', max_length=50, choices=CATEGORIES)
    phone_number = models.CharField('Phone number', max_length=15, blank=True, null=True)
    head = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, limit_choices_to={'roles__name': 'Head of Establishment'}, on_delete=models.SET_NULL, related_name='headed_establishments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_Establishments', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a créé')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_Establishments', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a mis à jour')
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = 'Establishment'
        verbose_name_plural = 'Establishments'

    def __str__(self):
        return self.name
