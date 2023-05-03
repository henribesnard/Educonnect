from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Timeslot
from .forms import TimeslotForm
from educonnect.permissions import head_or_staff_check
from django.contrib.auth.decorators import  user_passes_test

@user_passes_test(head_or_staff_check, login_url='/login/')
def timeslot_list(request):
    establishment = request.user.establishment
    timeslots = Timeslot.objects.filter(schoolclass__establishment=establishment)
    return render(request, 'gestion_emplois_temps/timeslot_list.html', {'timeslots': timeslots})

@user_passes_test(head_or_staff_check, login_url='/login/')
def timeslot_update(request, pk):
    timeslot = get_object_or_404(Timeslot, pk=pk, schoolclass__establishment=request.user.establishment)
    establishment = request.user.establishment
    if request.method == 'POST':
        form = TimeslotForm(request.POST, instance=timeslot, establishment=establishment)
        if form.is_valid():
            timeslot = form.save(commit=False)
            timeslot.updated_by = request.user
            timeslot.save()
            return redirect('timeslot_list')
    else:
        form = TimeslotForm(instance=timeslot, establishment=establishment)
    return render(request, 'timeslots/timeslot_form.html', {'form': form})


@user_passes_test(head_or_staff_check, login_url='/login/')
def timeslot_update(request, pk):
    timeslot = get_object_or_404(Timeslot, pk=pk, schoolclass__establishment=request.user.establishment)
    establishment = request.user.establishment
    if request.method == 'POST':
        form = TimeslotForm(request.POST, instance=timeslot, establishment=establishment)
        if form.is_valid():
            timeslot = form.save(commit=False)
            timeslot.updated_by = request.user
            timeslot.save()
            return redirect('timeslot_list')
    else:
        form = TimeslotForm(instance=timeslot, establishment=establishment)
    return render(request, 'timeslots/timeslot_form.html', {'form': form})

def timeslot_delete(request, pk):
    timeslot = get_object_or_404(Timeslot, pk=pk)
    timeslot.delete()
    messages.success(request, 'Le créneau horaire a été supprimé avec succès.')
    return redirect('timeslot_list')
