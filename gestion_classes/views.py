from django.shortcuts import get_object_or_404, render, redirect
from .models import Schoolclass, Course
from .forms import AddClassForm, AssignPrincipalTeacherForm, EditClassForm, CourseForm,EditCourseForm
from django.contrib import messages
from educonnect.permissions import admin_check
from django.contrib.auth.decorators import login_required, user_passes_test

@user_passes_test(admin_check, login_url='/login/')
def add_class(request):
    if request.method == "POST":
        form = AddClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            return redirect('ask_assign_teacher', class_id=new_class.id)
    else:
        form = AddClassForm()

    return render(request, 'gestion_classes/add_classe.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def ask_assign_teacher(request, class_id):
    schoolclass = get_object_or_404(Schoolclass, id=class_id)
    if request.method == "POST":
        if "yes" in request.POST:
            return redirect('assign_principal_teacher', class_id=class_id)
        elif "no" in request.POST:
            return redirect('classes_list')

    return render(request, 'gestion_classes/ask_assign_teacher.html', {'schoolclass': schoolclass})

@user_passes_test(admin_check, login_url='/login/')
def assign_principal_teacher(request, class_id):
    schoolclass = get_object_or_404(Schoolclass, id=class_id)
    if request.method == "POST":
        form = AssignPrincipalTeacherForm(request.POST, schoolclass=schoolclass)
        if form.is_valid():
            teacher = form.cleaned_data['principal_teacher']
            schoolclass.principal_teacher = teacher
            schoolclass.save()
            return redirect('classes_list')
    else:
        form = AssignPrincipalTeacherForm(schoolclass=schoolclass)

    return render(request, 'gestion_classes/assign_principal_teacher.html', {'form': form, 'schoolclass': schoolclass})

@user_passes_test(admin_check, login_url='/login/')
def classes_list(request):
    classes = Schoolclass.objects.all()
    return render(request, 'gestion_classes/classes_list.html', {'classes': classes})

@user_passes_test(admin_check, login_url='/login/')
def edit_class(request, class_id):
    schoolclass = get_object_or_404(Schoolclass, pk=class_id)
    if request.method == 'POST':
        form = EditClassForm(request.POST, instance=schoolclass, schoolclass=schoolclass)
        if form.is_valid():
            form.save()
            messages.success(request, 'La classe a été modifiée avec succès.')
            return redirect('classes_list')
    else:
        form = EditClassForm(instance=schoolclass, schoolclass=schoolclass)
    return render(request, 'gestion_classes/edit_classe.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def delete_class(request, class_id):
    schoolclass = get_object_or_404(Schoolclass, pk=class_id)
    if request.method == 'POST':
        schoolclass.delete()
        messages.success(request, 'La classe a été supprimée avec succès.')
        return redirect('classes_list')
    return render(request, 'gestion_classes/delete_classe.html', {'schoolclass': schoolclass})

@user_passes_test(admin_check, login_url='/login/')
def class_detail(request, class_id):
    schoolclass = get_object_or_404(Schoolclass, pk=class_id)
    students = schoolclass.students.all()
    context = {
        'schoolclass': schoolclass,
        'students': students,
    }
    return render(request, 'gestion_classes/classe_detail.html', context)

@user_passes_test(admin_check, login_url='/login/')
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Cours créé avec succès.')
            return redirect('courses_list')
    else:
        form = CourseForm()
    return render(request, 'gestion_classes/add_course.html', {'form': form})

@user_passes_test(admin_check, login_url='/login/')
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Cours supprimé avec succès.')
        return redirect('courses_list')
    return render(request, 'gestion_classes/delete_course.html', {'course': course})

@user_passes_test(admin_check, login_url='/login/')
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'gestion_classes/courses_list.html', {'courses': courses})

@user_passes_test(admin_check, login_url='/login/')
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    schoolclass = course.schoolclass

    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course, course=course)

        if form.is_valid():
            form.save()
            course.teachers.set(form.cleaned_data['teachers'])
            course.save()
            messages.success(request, 'Le cours a été modifié avec succès.')
            return redirect('courses_list')

    else:
        form = EditCourseForm(instance=course, course=course)
        form.fields['teachers'].initial = course.teachers.all()

    context = {
        'form': form,
        'course': course,
        'schoolclass': schoolclass,
    }

    return render(request, 'gestion_classes/edit_course.html', context)

@user_passes_test(admin_check, login_url='/login/')
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    teachers = course.teachers.all()

    context = {
        'course': course,
        'teachers': teachers,
    }

    return render(request, 'gestion_classes/course_detail.html', context)