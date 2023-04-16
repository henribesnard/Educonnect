from django.core.management.base import BaseCommand
from gestion_utilisateurs.models import User, Role
from etablissements.models import Establishment

class Command(BaseCommand):
    help = "Insère des utilisateurs de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets Role si nécessaire
        admin_role, _ = Role.objects.get_or_create(name='ADMIN')
        head_role, _ = Role.objects.get_or_create(name='HEAD')
        staff_role, _ = Role.objects.get_or_create(name='STAFF')
        parent_role, _ = Role.objects.get_or_create(name='PARENT')
        etudiant_role, _ = Role.objects.get_or_create(name='STUDENT')
        etablissement = Establishment.objects.first()
        

        # Créez les objets Utilisateur
        head = User.objects.create_user(username='head1', email='head1@example.com', last_name='head1', first_name='head1', password='head123', is_head=True)
        head.roles.add(head_role)
        head.establishment = etablissement
        head.save()

        staff = User.objects.create_user(username='staff1', email='staff1@example.com', last_name='staff1', first_name='staff1', password='staff123', is_staff=True)
        staff.roles.add(staff_role)
        staff.establishment = etablissement
        staff.save()

        parent = User.objects.create_user(username='parent5', email='parent5@example.com', last_name='parent5', first_name='parent5', password='parent123', is_parent=True)
        parent.roles.add(parent_role)
        parent.save()


        self.stdout.write(self.style.SUCCESS("Les utilisateurs de test ont été insérés avec succès."))

