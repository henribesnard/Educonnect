# Generated by Django 4.2 on 2023-04-19 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etablissements', '0002_initial'),
        ('gestion_classes', '0002_initial'),
        ('gestion_emplois_temps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_timeslots', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur qui a créé'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_emplois_temps.room', verbose_name='room'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='schoolclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_classes.schoolclass', verbose_name='schoolclass'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_timeslots', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur qui a mis à jour'),
        ),
        migrations.AddField(
            model_name='room',
            name='establishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissements.establishment', verbose_name='Établissement'),
        ),
    ]
