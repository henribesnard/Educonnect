
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

