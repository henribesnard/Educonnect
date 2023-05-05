from django.core.management.base import BaseCommand
from gestion_utilisateurs.models import User, Role
from etablissements.models import EstablishmentType, Establishment

class Command(BaseCommand):
    help = "Insère un teacher de test dans la base de données."

    def handle(self, *args, **options):
        # Créez des objets Role si nécessaire
       teacher_role, _ = Role.objects.get_or_create(name='TEACHER')
       student_role, _ = Role.objects.get_or_create(name ='STUDENT')
       parent_role, _ = Role.objects.get_or_create(name= 'PARENT')
        # Choisissez un établissement pour les utilisateurs (vous pouvez le modifier selon vos besoins)
       etablissement = Establishment.objects.first()

       teacher2 = User.objects.create_user(username='teacher2', email='teacher2@example.com', last_name='teacher2', first_name='teacher2', password='teacher123')
       teacher2.roles.add(teacher_role)
       teacher2.establishment = etablissement
       teacher2.save()


       student1 = User.objects.create_user(username='student1', email='student1@example.com', last_name='student1', first_name='student1', password='student123')
       student1.roles.add(student_role)
       student1.estblishment = etablissement
       student1.save()

       parent1 = User.objects.create_user(username='parent1', email='parent1@example.com', last_name='parent1', first_name='parent1', password='parent123')
       parent1.roles.add(parent_role)
       parent1.save()

       self.stdout.write(self.style.SUCCESS("les users de test ont été inséré avec succès."))



