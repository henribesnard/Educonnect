# Generated by Django 4.2 on 2023-04-26 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateurs', '0002_alter_user_establishment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile picture'),
        ),
    ]
