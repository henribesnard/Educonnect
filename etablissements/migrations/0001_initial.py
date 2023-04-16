# Generated by Django 4.2 on 2023-04-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('category', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], max_length=50, verbose_name='Category')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Establishment',
                'verbose_name_plural': 'Establishments',
            },
        ),
        migrations.CreateModel(
            name='EstablishmentType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('PRESCHOOL', 'Preschool'), ('PRIMARY', 'Primary'), ('MIDDLE_SCHOOL', 'Middle School'), ('HIGH_SCHOOL', 'High School'), ('UNIVERSITY', 'University'), ('INSTITUTE', 'Institute'), ('TRAINING_CENTER', 'Training Center')], max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Establishment Type',
                'verbose_name_plural': 'Establishment Types',
            },
        ),
    ]