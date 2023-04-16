from django.urls import path
from . import views

urlpatterns = [
    # URL pour gestion des classes ADMIN
    path('classes/', views.list_classes, name='classes_list'),
    path('classes/add/', views.add_class, name='add_class'),
    path('classes/update/<int:pk>/', views.update_class, name='update_class'),
    path('classes/delete/<int:pk>/', views.delete_class, name='delete_class'),

    # URL pour gestion des cours ADMIN
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('courses/delete/<int:pk>/', views.delete_course, name='delete_course'),

    # URL pour gestion des classes HEAD et STAFF
    path('staff/classes/add/', views.staff_add_class, name='staff_add_class'),
    path('staff/classes/view/<int:pk>/', views.staff_view_class, name='staff_view_class'),
    path('staff/classes/edit/<int:pk>/', views.staff_edit_class, name='staff_edit_class'),
    path('staff/classes/delete/<int:pk>/', views.staff_delete_class, name='staff_delete_class'),
]
