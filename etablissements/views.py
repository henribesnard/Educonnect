from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from .forms import EstablishmentForm, EstablishmentTypeForm
from .models import Establishment, EstablishmentType
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from educonnect.permissions import admin_check


@user_passes_test(admin_check, login_url='/login/')
def add_establishment(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        print("Before is_valid:", form['head'].value())  # Debug print statement

        if form.is_valid():
            print("After is_valid:", form.cleaned_data['head'])  # Debug print statement
            establishment = form.save(commit=False)
            establishment.created_by = request.user
            establishment.updated_by = request.user
            establishment.save()
            form.save_m2m()  # Pour sauvegarder les relations ManyToMany
            head = establishment.head
            send_mail(
                'Bienvenue sur notre plateforme',
                f"Cher {head.first_name},\n\nVous avez été désigné comme chef d'établissement pour {establishment.name}. Votre nom d'utilisateur est {head.username}. Utilisez-le pour accéder au tableau de bord.",
                'noreply@example.com',
                [head.email],
                fail_silently=False,
            )
            return redirect('establishment_list')
        else:
            print("Form errors:", form.errors)  # Debug print statement
    else:
        form = EstablishmentForm()
    return render(request, 'etablissements/add_establishment.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def establishment_list(request):
    establishments = Establishment.objects.all()
    return render(request, 'etablissements/establishment_list.html', {'establishments': establishments})

@user_passes_test(admin_check, login_url='/login/')
def establishment_update(request, establishment_id):
    establishment = get_object_or_404(Establishment, pk=establishment_id)
    if request.method == 'POST':
        form = EstablishmentForm(request.POST, instance=establishment)
        if form.is_valid():
            establishment = form.save(commit=False)
            establishment.updated_by = request.user
            establishment.save()
            form.save_m2m()
            return redirect('establishment_list')
    else:
        form = EstablishmentForm(instance=establishment)
    return render(request, 'etablissements/establishment_update.html', {'form': form, 'establishment': establishment})

@user_passes_test(admin_check, login_url='/login/')
def establishment_delete(request, establishment_id):
    establishment = get_object_or_404(Establishment, pk=establishment_id)
    if request.method == 'POST':
        establishment.delete()
        return redirect('establishment_list')
    return render(request, 'etablissements/establishment_delete.html', {'establishment': establishment})

@user_passes_test(admin_check, login_url='/login/')
def EstablishmentTypeCreateView(request):
    if request.method == 'POST':
        form = EstablishmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('establishment_type_list')
    else:
        form = EstablishmentTypeForm()
    return render(request, 'etablissements/establishment_type_form.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def EstablishmentTypeUpdateView(request, pk):
    establishmentType = get_object_or_404(EstablishmentType, pk=pk)
    if request.method == 'POST':
        form = EstablishmentTypeForm(request.POST, instance=establishmentType)
        if form.is_valid():
            form.save()
            return redirect('establishment_type_list')
    else:
        form = EstablishmentTypeForm(instance=establishmentType)
    return render(request, 'etablissements/establishment_type_form.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def EstablishmentTypeDeleteView(request, pk):
    establishmentType = get_object_or_404(EstablishmentType, pk=pk)
    establishmentType.delete()
    return redirect('establishment_type_list')
    
    
@user_passes_test(admin_check, login_url='/login/')
def EstablishmentTypeListView(request):
    establishmentTypes = EstablishmentType.objects.all()
    return render(request, 'etablissements/establishment_type_list.html', {'establishmentTypes': establishmentTypes})

@user_passes_test(admin_check, login_url='/login/')
def EstablishmentDetailView(request, pk):
    establishment = get_object_or_404(Establishment, pk=pk)
    return render(request, 'etablissements/establishment_detail.html', {'establishment': establishment})

@user_passes_test(admin_check, login_url='/login/')
def EstablishmentTypeDetailView(request, pk):
    establishmentType = get_object_or_404(EstablishmentType, pk=pk)
    return render(request, 'etablissements/establishment_type_detail.html', {'establishmentType': establishmentType})
                
                  
