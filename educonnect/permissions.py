from gestion_emplois_temps.models import Timeslot

def admin_check(user):
    return user.is_authenticated and user.is_admin

def head_or_staff_check(user):
    return user.is_authenticated and (user.is_head or user.is_staff)

def head_check(user):
    return user.is_authenticated and user.is_head

def staff_check(user):
    return user.is_authenticated and user.is_staff

def teacher_check(user):
    return user.is_authenticated and user.is_teacher

def parent_check(user):
    return user.is_authenticated and user.is_parent

def student_check(user):
    return user.is_authenticated and user.is_student

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

