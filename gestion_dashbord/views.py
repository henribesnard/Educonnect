from django.shortcuts import render
from django.contrib.auth.decorators import  login_required

@login_required
def dashboard(request):
    user_roles = request.user.roles.values_list('name', flat=True)
    return render(request, 'gestion_dashbord/dashboard.html', {'user_roles': user_roles})

