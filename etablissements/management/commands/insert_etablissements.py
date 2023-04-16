# insert_etablissements.py
from django.core.management.base import BaseCommand
from etablissements.models import Establishment, EstablishmentType

class Command(BaseCommand):
    help = "Insère des établissements de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets TypeEtablissement si nécessaire
        type_etablissement, _ = EstablishmentType.objects.get_or_create(name='COLLEGE')

        # Créez les objets Etablissement
        etablissement_a = Establishment(name='Etablissement A', address='address A', category='PUBLIC')
        etablissement_a.save()
        etablissement_a.types.add(type_etablissement)

        etablissement_b = Establishment(name='Etablissement B', address='address B', category='PUBLIC')
        etablissement_b.save()
        etablissement_b.types.add(type_etablissement)

        etablissement_c = Establishment(name='Etablissement C', address='address C', category='PRIVE')
        etablissement_c.save()
        etablissement_c.types.add(type_etablissement)

        etablissement_d = Establishment(name='Etablissement D', address='address D', category='PRIVE')
        etablissement_d.save()
        etablissement_d.types.add(type_etablissement)

        self.stdout.write(self.style.SUCCESS("Les établissements de test ont été insérés avec succès."))
