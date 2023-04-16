from django.core.management.base import BaseCommand
from gestion_utilisateurs.models import User, Role
from etablissements.models import Establishment

class Command(BaseCommand):
    help = "Insère des utilisateurs de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets Role si nécessaire
        admin_role, _ = Role.objects.get_or_create(name='ADMIN')

        # Créez les objets Utilisateur
        admin = User.objects.create_user(username='admin', email='admin@example.com', last_name='Admin', first_name='Admin', password='admin123', is_admin=True)
        admin.roles.add(admin_role)
        admin.save()


        self.stdout.write(self.style.SUCCESS("Les utilisateurs de test ont été insérés avec succès."))

