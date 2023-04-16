from django import forms
from .models import Schoolclass, Course
from django.contrib.auth import get_user_model

class SchoolclassForm(forms.ModelForm):
    class Meta:
        model = Schoolclass
        fields = ['name', 'establishment', 'principal_teacher', 'level']

class StaffSchoolclassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(StaffSchoolclassForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['principal_teacher'].queryset = user.establishment.staff.filter(role='ENSEIGNANT')

    class Meta:
        model = Schoolclass
        fields = ('name', 'level', 'principal_teacher', 'students')
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'schoolclass', 'subject', 'teachers', 'description']

class StaffCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'schoolclass', 'subject', 'teachers', 'description']

    def __init__(self, *args, **kwargs):
        establishment = kwargs.pop('establishment', None)
        super().__init__(*args, **kwargs)
        self.fields['schoolclass'].queryset = Schoolclass.objects.filter(establishment=establishment)
        self.fields['teachers'].queryset = get_user_model().objects.filter(establishment=establishment, roles='TEACHER')

