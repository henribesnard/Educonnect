from django.core.management.base import BaseCommand
from gestion_utilisateurs.models import User, Role
from etablissements.models import EstablishmentType, Establishment

class Command(BaseCommand):
    help = "Insère un admin de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets Role si nécessaire
        head_role, _ = Role.objects.get_or_create(name='HEAD')

        head1 = User.objects.create_user(username='head1', email='head1@example.com', last_name='head1', first_name='head1', password='head123')
        head1.roles.add(head_role)
        head1.save()

        self.stdout.write(self.style.SUCCESS("head de test ont été inséré avec succès."))