# Generated by Django 4.2 on 2023-04-16 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_classes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(limit_choices_to={'roles__name': 'Teacher'}, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='principal_teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'roles__name': 'Teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'roles__name': 'Student'}, related_name='classes', to=settings.AUTH_USER_MODEL),
        ),
    ]
