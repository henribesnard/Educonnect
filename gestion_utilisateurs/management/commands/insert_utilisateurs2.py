from django.core.management.base import BaseCommand
from gestion_utilisateurs.models import User, Role
from etablissements.models import Establishment
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Insère des utilisateurs de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets Role si nécessaire
        parent_role, _ = Role.objects.get_or_create(name='PARENT')
        etudiant_role, _ = Role.objects.get_or_create(name='STUDENT')

        # Choisissez un établissement pour les utilisateurs (vous pouvez le modifier selon vos besoins)
        etablissement = Establishment.objects.first()

        etudiant1 = User.objects.create_user(username='etudiant1', email='etudiant1@example.com', last_name='Etudiant1', first_name='Etudiant1', password='Etudiant12@', is_student=True, address='2 Rue des Etudiants', phone_number='+33123456786',date_of_birth=datetime.today() - timedelta(days=365 * 10))
        etudiant1.roles.add(etudiant_role)
        etudiant1.establishment = etablissement
        etudiant1.save()
        
        etudiant3 = User.objects.create_user(username='etudiant3', email='etudiant3@example.com', last_name='etudiant3', first_name='Etudiant1', password='Etudiant12@', is_student=True, address='2 Rue des Etudiants', phone_number='+33123456786',date_of_birth=datetime.today() - timedelta(days=365 * 10))
        etudiant3.roles.add(etudiant_role)
        etudiant3.establishment = etablissement
        etudiant3.save()

        etudiant2 = User.objects.create_user(username='etudiant2', email='etudiant2@example.com', last_name='Etudiant2', first_name='Etudiant2', password='Etudiant12@', is_student=True, address='3 Rue des Etudiants', phone_number='+33123456786',date_of_birth=datetime.today() - timedelta(days=365 * 15))
        etudiant2.roles.add(etudiant_role)
        etudiant2.establishment = etablissement
        etudiant2.save()

        parent1 = User.objects.create_user(username='parent1', email='parent1@example.com', last_name='parent1', first_name='parent1', password='Parent123@', is_parent=True, address='2 Rue des Etudiants', phone_number='+33123456786',date_of_birth=datetime.today() - timedelta(days=365 * 60))
        parent1.roles.add(parent_role)
        parent1.save()

        # Associer l'étudiant1 au parent1 
        parent1.children.add(etudiant1)
        parent1.save()

        parent2 = User.objects.create_user(username='parent2', email='parent2@example.com', last_name='parent2', first_name='parent2', password='Parent123@', is_parent=True, address='3 Rue des Etudiants', phone_number='+33123456786',date_of_birth=datetime.today() - timedelta(days=365 * 60))
        parent2.roles.add(parent_role)
        parent2.save()

        # Associer l'étudiant2 et 3  au parent2 
        parent2.children.add(etudiant2)
        parent2.save()

        parent2.children.add(etudiant3)
        parent2.save()

        self.stdout.write(self.style.SUCCESS("Les utilisateurs de test ont été insérés avec succès."))