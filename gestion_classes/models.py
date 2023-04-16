from django.db import models
from django.conf import settings
from etablissements.models import Establishment

class Schoolclass(models.Model):
    LEVELS = (
        ('MAT1', 'MATERNELLE 1'),
        ('MAT2', 'MATERNELLE 2'),
        ('C1', 'PRIMAIRE C1'),
        ('CP', 'PRIMAIRE CP'),
        ('CE1', 'PRIMAIRE CE1'),
        ('CE2', 'PRIMAIRE CE2'),
        ('CM1', 'PRIMAIRE CM1'),
        ('CM2', 'PRIMAIRE CM2'),
        ('6EME', 'SECONDAIRE 6EME'),
        ('5EME', 'SECONDAIRE 5EME'),
        ('4EME', 'SECONDAIRE 4EME'),
        ('3EME', 'SECONDAIRE 3EME'),
        ('2ND', 'SECONDAIRE 2ND'),
        ('1ERE', 'SECONDAIRE 1ERE'),
        ('TERMINAL', 'SECONDAIRE TERMINAL'),
        ('L1', 'UNIVERSITAIRE LICENCE1'),
        ('L2', 'UNIVERSITAIRE LICENCE2'),
        ('L3', 'UNIVERSITAIRE LICENCE3'),
        ('M1', 'UNIVERSITAIRE MASTER1'),
        ('M2', 'UNIVERSITAIRE MASTER2'),
    )

    name = models.CharField(max_length=255)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, limit_choices_to={'roles__name': 'Student'}, related_name='classes')
    principal_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, limit_choices_to={'roles__name': 'Teacher'}, on_delete=models.SET_NULL, related_name='teacher_classes')
    level = models.CharField(max_length=8, choices=LEVELS)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_classes', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a créé')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_Classes', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a mis à jour')

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return self.name

class Course(models.Model):
    SUBJECTS = (
        ('MATH', 'Mathématiques'),
        ('PHYS', 'Physique'),
        ('CHIM', 'Chimie'),
        ('BIO', 'Biologie'),
        ('HIST', 'Histoire'),
        ('GEO', 'Géographie'),
        # Ajoutez d'autres matières si nécessaire
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    schoolclass = models.ForeignKey(Schoolclass, on_delete=models.CASCADE)
    subject = models.CharField(max_length=4, choices=SUBJECTS)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, limit_choices_to={'roles__name': 'Teacher'})
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name