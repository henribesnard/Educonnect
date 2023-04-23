from gestion_emplois_temps.models import Timeslot

def admin_check(user):
    return user.is_authenticated and user.roles.filter(name='ADMIN').exists()

def head_or_staff_check(user):
    return user.is_authenticated and (user.roles.filter(name='HEAD').exists() or user.roles.filter(name='STAFF').exists())

def head_staff_teacher_check(user):
    return user.is_authenticated and (user.roles.filter(name='HEAD').exists() or user.roles.filter(name='STAFF').exists() or user.roles.filter(name='TEACHER').exists())

def head_check(user):
    return user.is_authenticated and user.roles.filter(name='HEAD').exists()

def staff_check(user):
    return user.is_authenticated and user.roles.filter(name='STAFF').exists()

def teacher_check(user):
    return user.is_authenticated and user.roles.filter(name='TEACHER').exists()

def parent_check(user):
    return user.is_authenticated and user.roles.filter(name='PARENT').exists()

def student_check(user):
    return user.is_authenticated and user.roles.filter(name='STUDENT').exists()

def check_class_availability(schoolclass, start_datetime, end_datetime, timeslot_id=None):
    overlapping_slots = Timeslot.objects.filter(
        schoolclass=schoolclass,
        start_datetime__lt=end_datetime,
        end_datetime__gt=start_datetime
    ).exclude(pk=timeslot_id)

    if overlapping_slots.exists():
        return False
    return True

def check_room_availability(room, start_datetime, end_datetime, timeslot_id=None):
    overlapping_rooms = Timeslot.objects.filter(
        room=room,
        start_datetime__lt=end_datetime,
        end_datetime__gt=start_datetime
    ).exclude(pk=timeslot_id)

    if overlapping_rooms.exists():
        return False
    return True
