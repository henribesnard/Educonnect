from django.shortcuts import render
from educonnect.permissions import admin_check, head_check, staff_check, teacher_check, parent_check, student_check
from django.contrib.auth.decorators import  user_passes_test

@user_passes_test(admin_check, login_url='/login/')
def admin_dashboard(request):
    return render(request, 'gestion_dashbord/admin_dashboard.html')

@user_passes_test(head_check, login_url='/login/')
def head_dashboard(request):
    return render(request, 'gestion_dashbord/head_dashboard.html')

@user_passes_test(staff_check, login_url='/login/')
def staff_dashboard(request):
    return render(request, 'gestion_dashbord/staff_dashboard.html')

@user_passes_test(teacher_check, login_url='/login/')
def teacher_dashboard(request):
    return render(request, 'gestion_dashbord/teacher_dashboard.html')

@user_passes_test(parent_check, login_url='/login/')
def parent_dashboard(request):
    return render(request, 'gestion_dashbord/parent_dashboard.html')

@user_passes_test(student_check, login_url='/login/')
def student_dashboard(request):
    return render(request, 'gestion_dashbord/student_dashboard.html')