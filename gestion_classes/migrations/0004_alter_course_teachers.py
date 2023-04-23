# Generated by Django 4.2 on 2023-04-21 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_classes', '0003_alter_schoolclass_principal_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'roles__name': 'Teacher'}, to=settings.AUTH_USER_MODEL),
        ),
    ]
