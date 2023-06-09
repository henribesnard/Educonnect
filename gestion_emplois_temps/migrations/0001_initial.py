# Generated by Django 4.2 on 2023-04-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('capacity', models.IntegerField(blank=True, null=True, verbose_name='Capacité')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField(verbose_name='Date et heure de début')),
                ('end_datetime', models.DateTimeField(verbose_name='Date et heure de fin')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_classes.course', verbose_name='subject')),
            ],
            options={
                'verbose_name': 'Timeslot',
                'verbose_name_plural': 'Timeslots',
            },
        ),
    ]
