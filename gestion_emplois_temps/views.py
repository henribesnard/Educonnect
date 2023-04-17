from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Timeslot
from .forms import TimeslotForm
from django.contrib.auth.decorators import  user_passes_test
from educonnect.permissions import admin_check
from django.http import JsonResponse
import datetime
from .models import Schoolclass

# Ajouter un emploi du temps
@user_passes_test(admin_check, login_url='/login/')
def add_timeslot(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeslots_list')
    else:
        form = TimeslotForm()
    return render(request, 'gestion_empois_temps/add_timeslot.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
# Lister les emplois du temps
def timeslots_list(request):
    timeslots = Timeslot.objects.all()
    return render(request, 'gestion_empois_temps/timeslots_list.html', {'timeslots': timeslots})

@user_passes_test(admin_check, login_url='/login/')
# Modifier un emploi du temps
def edit_timeslot(request, pk):
    timeslot = get_object_or_404(Timeslot, pk=pk)
    if request.method == 'POST':
        form = TimeslotForm(request.POST, instance=timeslot)
        if form.is_valid():
            form.save()
            return redirect('timeslots_list')
    else:
        form = TimeslotForm(instance=timeslot)
    return render(request, 'gestion_empois_temps/edit_timeslot.html', {'form': form})

# Supprimer un emploi du temps
@user_passes_test(admin_check, login_url='/login/')
def delete_timeslot(request, pk):
    timeslot = get_object_or_404(Timeslot, pk=pk)
    if request.method == 'POST':
        timeslot.delete()
        return redirect('timeslots_list')
    return render(request, 'gestion_empois_temps/delete_timeslot.html', {'timeslot': timeslot})


def get_available_rooms(request):
    """
    Cette vue récupère les salles disponibles en fonction des dates et heures de début et de fin,
    et de l'établissement de la classe. Les données sont renvoyées au format JSON.
    """
    start_datetime = request.GET.get('start_datetime')
    end_datetime = request.GET.get('end_datetime')
    schoolclass_id = request.GET.get('schoolclass_id')

    if start_datetime and end_datetime and schoolclass_id:
        start_datetime = datetime.datetime.fromisoformat(start_datetime)
        end_datetime = datetime.datetime.fromisoformat(end_datetime)
        schoolclass = Schoolclass.objects.get(pk=schoolclass_id)

        available_rooms = TimeslotForm().get_available_rooms(start_datetime, end_datetime, schoolclass)

        rooms_json = [{'id': room.id, 'name': room.name} for room in available_rooms]

        return JsonResponse(rooms_json, safe=False)

