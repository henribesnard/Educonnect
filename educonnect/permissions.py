
def admin_check(user):
    return user.is_authenticated and user.is_admin

def head_or_staff_check(user):
    return user.is_authenticated and (user.is_head or user.is_staff)