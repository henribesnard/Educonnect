from django.urls import path
from . import views

urlpatterns = [
    path('classes_list', views.classes_list, name='classes_list'),
    path('add_class', views.add_class, name='add_class'),
    path('assign_principal_teacher/<int:class_id>/', views.assign_principal_teacher, name='assign_principal_teacher'),
    path('classes_list/', views.classes_list, name='classes_list'),
    path('ask_assign_teacher/<int:class_id>/', views.ask_assign_teacher, name='ask_assign_teacher'),
    path('edit_class/<int:class_id>/', views.edit_class, name='edit_class'),
    path('delete_class/<int:class_id>/', views.delete_class, name='delete_class'),
    path('class_detail/<int:class_id>/', views.class_detail, name='class_detail'),

    path('add_course/', views.create_course, name='add_course'),
    path('list/', views.courses_list, name='courses_list'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
]
