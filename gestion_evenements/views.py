from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Event
from .forms import EventForm
from educonnect.permissions import admin_check

@user_passes_test(admin_check, login_url='/login/')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('events_list')
    else:
        form = EventForm()
    return render(request, 'gestion_evenements/add_event.html', {'form': form})


@user_passes_test(admin_check, login_url='/login/')
def events_list(request):
    events = Event.objects.filter(organizer=request.user).order_by('start_date')
    return render(request, 'gestion_evenements/events_list.html', {'events': events})


@user_passes_test(admin_check, login_url='/login/')
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'gestion_evenements/edit_event.html', {'form': form})


@user_passes_test(admin_check, login_url='/login/')
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    return render(request, 'gestion_evenements/delete_event.html', {'event': event})
