from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404
from .models import Schoolclass, Course
from django.contrib.auth.decorators import login_required, user_passes_test
from educonnect.permissions import admin_check, head_or_staff_check
from .models import Schoolclass
from .forms import SchoolclassForm, StaffSchoolclassForm, CourseForm, StaffCourseForm

# vues pour les classes accessibles aux ADMIN
@user_passes_test(admin_check, login_url='/login/')
def list_classes(request):
    classes = Schoolclass.objects.all()
    context = {'classes': classes}
    return render(request, 'gestion_classes/classes_list.html', context)

@user_passes_test(admin_check, login_url='/login/')
def add_class(request):
    if request.method == 'POST':
        form = SchoolclassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.created_by = request.user
            new_class.save()
            return redirect('classes_list')
    else:
        form = SchoolclassForm()

    context = {'form': form}
    return render(request, 'gestion_classes/add_class.html', context)

@user_passes_test(admin_check, login_url='/login/')
def update_class(request, pk):
    schoolclass = get_object_or_404(Schoolclass, pk=pk)
    if request.method == 'POST':
        form = SchoolclassForm(request.POST, instance=schoolclass)
        if form.is_valid():
            form.save()
            return redirect('classes_list')  # Redirigez vers la vue appropriée après la mise à jour
    else:
        form = SchoolclassForm(instance=schoolclass)
    return render(request, 'gestion_classes/update_class.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def delete_class(request, pk):
    schoolclass = get_object_or_404(Schoolclass, pk=pk)
    if request.method == 'POST':
        schoolclass.delete()
        return redirect('classes_list')  # Redirigez vers la vue appropriée après la suppression
    return render(request, 'gestion_classes/delete_class.html', {'schoolclass': schoolclass})

# vues pour les classes accessibles au HEAD et STAFF

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_add_class(request):
    user = request.user
    if request.method == 'POST':
        form = SchoolclassForm(user=request.user)
        if form.is_valid():
            schoolclass = form.save(commit=False)
            schoolclass.establishment = user.establishment
            schoolclass.save()
            return redirect('staff_classes_list')
    else:
        form = StaffSchoolclassForm()
    return render(request, 'gestion_classes/staff_add_class.html', {'form': form}) 

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_view_class(request, pk):
    user = request.user
    try:
        schoolclass = Schoolclass.objects.get(pk=pk, establishment=user.establishment)
    except Schoolclass.DoesNotExist:
        raise Http404("La classe n'existe pas ou vous n'avez pas la permission de la voir.")
    return render(request, 'gestion_classes/staff_view_class.html', {'schoolclass': schoolclass})

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_edit_class(request, pk):
    user = request.user
    schoolclass = get_object_or_404(Schoolclass, pk=pk, establishment=user.establishment)
    if request.method == 'POST':
        form = StaffSchoolclassForm(instance=schoolclass, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('staff_classes_list')
    else:
        form = StaffSchoolclassForm(instance=schoolclass)
    return render(request, 'gestion_classes/staff_edit_class.html', {'form': form})

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_delete_class(request, pk):
    user = request.user
    schoolclass = get_object_or_404(Schoolclass, pk=pk, establishment=user.establishment)
    if request.method == 'POST':
        schoolclass.delete()
        return redirect('staff_classes_list')
    return render(request, 'gestion_classes/staff_delete_class.html', {'schoolclass': schoolclass})

#vues pour les cours accessibles aux admins
@user_passes_test(admin_check, login_url='/login/')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'gestion_classes/course_list.html', {'courses': courses})

@user_passes_test(admin_check, login_url='/login/')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'gestion_classes/add_course.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'gestion_classes/edit_course.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'gestion_classes/delete_course.html', {'course': course})

#Vues pour la gestion cours par les STAFF et HEAD
@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_courses_list(request):
    user = request.user
    courses = Course.objects.filter(schoolclass__establishment=user.establishment)
    return render(request, 'gestion_classes/staff_courses_list.html', {'courses': courses})

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_add_course(request):
    user = request.user
    if request.method == 'POST':
        form = StaffCourseForm(request.POST, establishment=user.establishment)
        if form.is_valid():
            form.save()
            return redirect('staff_courses_list')
    else:
        form = StaffCourseForm(establishment=user.establishment)
    return render(request, 'gestion_classes/staff_add_course.html', {'form': form})

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_edit_course(request, pk):
    user = request.user
    course = get_object_or_404(Course, pk=pk, schoolclass__establishment=user.establishment)
    if request.method == 'POST':
        form = StaffCourseForm(request.POST, instance=course, establishment=user.establishment)
        if form.is_valid():
            form.save()
            return redirect('staff_courses_list')
    else:
        form = StaffCourseForm(instance=course, establishment=user.establishment)
    return render(request, 'gestion_classes/staff_edit_course.html', {'form': form})

@user_passes_test(head_or_staff_check, login_url='/login/')
def staff_delete_course(request, pk):
    user = request.user
    course = get_object_or_404(Course, pk=pk, schoolclass__establishment=user.establishment)
    if request.method == 'POST':
        course.delete()
        return redirect('staff_courses_list')
    return render(request, 'gestion_classes/staff_delete_course.html', {'course': course})

