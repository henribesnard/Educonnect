from django.db import models
from django.conf import settings


class Assessment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    description = models.TextField('Description', blank=True, null=True)
    date = models.DateField('Date')
    total_points = models.PositiveIntegerField('Total Points')
    course = models.ForeignKey('gestion_classes.Course', on_delete=models.CASCADE, related_name='assessments')

    class Meta:
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'

    def __str__(self):
        return self.name

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Student', limit_choices_to={'roles': 'STUDENT'})
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, verbose_name='Assessment')
    points_obtained = models.DecimalField("Points Obtained", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

    def __str__(self):
        return f"{self.student} - {self.assessment} - {self.points_obtained}"

class Performance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Student', limit_choices_to={'roles': 'STUDENT'})
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, verbose_name='Assessment')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Grade')
    comment = models.TextField('Comment', blank=True, null=True)

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performances'

    def __str__(self):
        return f"{self.student} - {self.assessment} - {self.grade}"
