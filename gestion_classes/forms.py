from django import forms
from django.conf import settings
from .models import Schoolclass, Course
from gestion_utilisateurs.models import  Role, User

class AddClassForm(forms.ModelForm):
    class Meta:
        model = Schoolclass
        fields = ['name', 'establishment', 'level']

class AssignPrincipalTeacherForm(forms.ModelForm):
    class Meta:
        model = Schoolclass
        fields = ['principal_teacher']

    def __init__(self, *args, **kwargs):
        schoolclass = kwargs.pop('schoolclass', None)
        super(AssignPrincipalTeacherForm, self).__init__(*args, **kwargs)
        if schoolclass and schoolclass.establishment:
            # Récupérer le rôle "Teacher"
            teacher_role = Role.objects.get(name='TEACHER')
            
            # Filtrer les utilisateurs ayant le profil d'enseignant et appartenant au même établissement
            self.fields['principal_teacher'].queryset = User.objects.filter(
                roles=teacher_role, establishment=schoolclass.establishment
            )
        else:
            self.fields['principal_teacher'].queryset = User.objects.none()


class EditClassForm(forms.ModelForm):
    class Meta:
        model = Schoolclass
        fields = ['name', 'principal_teacher', 'level']

    def __init__(self, *args, **kwargs):
        schoolclass = kwargs.pop('schoolclass', None)
        super(EditClassForm, self).__init__(*args, **kwargs)
        if schoolclass and schoolclass.establishment:
            self.fields['principal_teacher'].queryset = User.objects.filter(
                roles__name='TEACHER',
                establishment=schoolclass.establishment
            )
        else:
            self.fields['principal_teacher'].queryset = User.objects.none()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'schoolclass', 'subject', 'description']

class EditCourseForm(CourseForm):
    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course')
        super(EditCourseForm, self).__init__(*args, **kwargs)
        self.fields['teachers'] = forms.ModelMultipleChoiceField(
            queryset=User.objects.filter(roles__name='TEACHER', establishment=course.schoolclass.establishment),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
