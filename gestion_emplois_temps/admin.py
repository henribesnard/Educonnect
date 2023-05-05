from django.contrib import admin
from .models import Timeslot, Room

@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass