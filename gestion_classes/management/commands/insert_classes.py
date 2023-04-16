from django.core.management.base import BaseCommand
from gestion_classes.models import Schoolclass, Course
from etablissements.models import Establishment

class Command(BaseCommand):
    help = "Insère des utilisateurs de test dans la base de données."

    def handle(self, *args, **options):

        # Choisissez un établissement pour les classes (vous pouvez le modifier selon vos besoins)
        etablissement = Establishment.objects.first()

        # Créez les objets classe
        classe1 = Schoolclass.objects.create(name = 'classe1', level = 'CM2')
        classe1.establishment = etablissement
        classe1.save()

        classe2 = Schoolclass.objects.create(name = 'classe2', level = 'CM1')
        classe2.establishment = etablissement
        classe2.save()

  

        self.stdout.write(self.style.SUCCESS("Les classes de test ont été insérés avec succès."))

