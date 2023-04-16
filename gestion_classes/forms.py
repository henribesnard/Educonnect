from django import forms
from .models import Schoolclass, Course

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
