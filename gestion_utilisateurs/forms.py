import string
from django.core.exceptions import ValidationError
from .models import User, Role
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserProfileForm(forms.ModelForm):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput,
        required=False,
        min_length=10
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'phone_number')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Username already exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_new_password(self):
        password = self.cleaned_data['new_password']
        if password:
            if not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
                raise ValidationError("Password must have at least one uppercase letter, one lowercase letter, one digit and one special character.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['new_password']:
            user.set_password(self.cleaned_data['new_password'])
        if commit:
            user.save()
        return user
    

class ModifierProfilEnfantForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'phone_number'] 

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomUserForm(UserCreationForm):

    roles = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        widget=forms.Select,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            'last_name', 'first_name', 'email',
            'address', 'date_of_birth', 'phone_number', 'roles', 'establishment',
            'is_student', 'is_teacher', 'is_admin', 'is_head', 'is_staff', 'is_parent', 'is_active'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = User.generate_username(user.first_name, user.last_name)
        user.set_password(User.generate_temporary_password())

        if commit:
            user.save()
            self.save_m2m()

        return user

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)
        
class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'roles', 'establishment', 'is_active')
