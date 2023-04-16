# Generated by Django 4.2 on 2023-04-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('status', models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('LATE', 'Late'), ('EXCUSED', 'Excused')], default='PRESENT', max_length=10, verbose_name='Status')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_classes.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
    ]
