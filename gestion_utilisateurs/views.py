import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import UserProfileForm, ModifierProfilEnfantForm, LoginForm, StudentRegistrationForm, CustomUserForm, CustomUserUpdateForm, RoleForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import User, Role
from django.core.mail import send_mail
from educonnect.permissions import admin_check, head_or_staff_check


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.roles.filter(name='ADMIN').exists():
                return redirect('admin_dashboard')
            elif user.roles.filter(name='HEAD').exists():
                return redirect('head_dashboard')
            elif user.roles.filter(name='STAFF').exists():
                return redirect('staff_dashboard')
            elif user.roles.filter(name='TEACHER').exists():
                return redirect('teacher_dashboard')
            elif user.roles.filter(name='PARENT').exists():
                return redirect('parent_dashboard')
            elif user.roles.filter(name='STUDENT').exists():
                return redirect('student_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'gestion_utilisateurs/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'gestion_utilisateurs/dashboard.html')

@login_required
def edit_profile(request):
    user = request.user

    if user.roles.filter(name='STUDENT').exists() and user.date_of_birth and (user.date_of_birth.year + 14 > datetime.date.today().year):
        if not any(parent == request.user for parent in user.children.all()):
            messages.error(request, "You are not authorized to modify this profile.")
            return redirect('dashboard')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            # Enregistrer l'utilisateur qui a mis à jour le profil
            user.updated_by = request.user
            # Enregistrer la date et l'heure actuelles dans le champ updated_at
            user.updated_at = timezone.now()
            user.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'gestion_utilisateurs/edit_profile.html', {'form': form})

@login_required
def profil_enfant(request, child_id):
    parent = request.user
    enfant = get_object_or_404(User, id=child_id)

    if parent.is_parent and enfant in parent.children.all():
        age = (timezone.now().date() - enfant.date_of_birth).days // 365
        modifiable = age < 14
        return render(request, 'gestion_utilisateurs/profil_enfant.html', {'enfant': enfant, 'modifiable': modifiable})
    else:
        return HttpResponseForbidden("Accès refusé.")

@login_required
def modifier_profil_enfant(request, child_id):
    parent = request.user
    enfant = get_object_or_404(User, id=child_id)

    if parent.is_parent and enfant in parent.children.all():
        age = (timezone.now().date() - enfant.date_of_birth).days // 365
        if age < 14:
            if request.method == "POST":
                form = ModifierProfilEnfantForm(request.POST, instance=enfant)
                if form.is_valid():
                    user = form.save(commit=False)
                    # Enregistrer l'utilisateur qui a mis à jour le profil
                    user.updated_by = request.user
                    # Enregistrer la date et l'heure actuelles dans le champ updated_at
                    user.updated_at = timezone.now()
                    user.save()
                    messages.success(request, "Le profil de l'enfant a été modifié avec succès.")
                    return redirect('profil_enfant', child_id=enfant.id)
            else:
                form = ModifierProfilEnfantForm(instance=enfant)
            return render(request, 'gestion_utilisateurs/modifier_profil_enfant.html', {'form': form})
        else:
            return HttpResponseForbidden("Accès refusé.")
    else:
        return HttpResponseForbidden("Accès refusé.")
    
@user_passes_test(head_or_staff_check, login_url='/login/')
def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.username = User.generate_username(student.first_name, student.last_name)
            student.password = User.generate_temporary_password()
            student.set_password(student.password)
            student.establishment = request.user.establishment  # Ajout de cette ligne
            student.save()

            student_role = Role.objects.get(name='STUDENT')
            student.roles.add(student_role)
            student.is_student = True
            student.save()

            send_mail(
                'Inscription réussie',
                f"Cher {student.first_name},\n\nVotre inscription en tant qu'étudiant a été réussie. Votre nom d'utilisateur est {student.username} et votre mot de passe temporaire est {student.password}. Utilisez ces informations pour vous connecter et n'oubliez pas de changer votre mot de passe après votre première connexion.",
                'noreply@example.com',
                [student.email],
                fail_silently=False,
            )
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'gestion_utilisateurs/register_student.html', {'form': form})

@user_passes_test(admin_check)
def user_list(request):
    users = User.objects.all()
    return render(request, 'gestion_utilisateurs/user_list.html', {'users': users})

@user_passes_test(admin_check)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'gestion_utilisateurs/user_create.html', {'form': form})

@user_passes_test(admin_check)
def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserUpdateForm(instance=user)
    return render(request, 'gestion_utilisateurs/user_update.html', {'form': form, 'user': user})

@user_passes_test(admin_check)
def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')

@user_passes_test(admin_check)
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'gestion_utilisateurs/role_list.html', {'roles': roles})

@user_passes_test(admin_check)
def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'gestion_utilisateurs/role_form.html', {'form': form})

@user_passes_test(admin_check)
def role_update(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'gestion_utilisateurs/role_form.html', {'form': form})

@user_passes_test(admin_check)
def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    role.delete()
    return redirect('role_list')