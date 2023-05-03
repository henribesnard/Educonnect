from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from etablissements.models import Establishment
import string
import secrets
from django.utils import timezone

class Role(models.Model):
    NAMES = (
        ('ADMIN', 'Admin'),
        ('HEAD', 'Head of Establishment'),
        ('STAFF', 'Staff'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
        ('STUDENT', 'Student'),
    )

    name = models.CharField('Name', max_length=50, choices=NAMES, unique=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(_('Username'), unique=True, max_length=150)
    last_name = models.CharField(_('Last name'), max_length=150, blank=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    email = models.EmailField(_('Email'), unique=True)
    password = models.CharField(_('Password'), max_length=128)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(_('Date of birth'), null=True, blank=True)
    phone_number = models.CharField(_('Phone number'), max_length=20, blank=True, null=True)
    roles = models.ManyToManyField(Role, verbose_name='Roles', blank=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.SET_NULL, verbose_name='Establishment', blank=True, null=True)
    children = models.ManyToManyField('self', verbose_name='Children', blank=True, symmetrical=False)
    is_principal_teacher = models.BooleanField(_('Principal Teacher'), default=False)
    position = models.CharField(_('Position'), max_length=200, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey('self', related_name='created_users', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a créé')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date de mise à jour')
    updated_by = models.ForeignKey('self', related_name='updated_users', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Utilisateur qui a mis à jour')
    profile_picture = models.ImageField(_('Profile picture'), upload_to='profile_pictures/', blank=True, null=True)
    is_active = models.BooleanField(_('Active'), default=True)

    @staticmethod
    def generate_temporary_password(length=10):
        if length < 10:
            raise ValueError("Password length should be at least 10")

        # Création de différents ensembles de caractères
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        special_characters = string.punctuation

        # Sélection aléatoire d'au moins un caractère de chaque ensemble
        password = [
            secrets.choice(uppercase_letters),
            secrets.choice(lowercase_letters),
            secrets.choice(digits),
            secrets.choice(special_characters)
        ]

        # Compléter le mot de passe avec des caractères aléatoires
        for i in range(length - 4):
            password.append(secrets.choice(uppercase_letters + lowercase_letters + digits + special_characters))

        # Mélanger les caractères pour obtenir un mot de passe complexe
        secrets.SystemRandom().shuffle(password)

        # Convertir la liste de caractères en chaîne
        return ''.join(password)

    @staticmethod
    def generate_username(first_name, last_name):
        base_username = f"{first_name[:1]}{last_name[:5]}".lower()
        username = base_username
        index = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{index}"
            index += 1

        return username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
