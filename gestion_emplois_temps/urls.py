from django.urls import path
from . import views

urlpatterns = [
    path('timeslots/add/', views.add_timeslot, name='add_timeslot'),
    path('timeslots/', views.timeslots_list, name='timeslots_list'),
    path('timeslots/edit/<int:pk>/', views.edit_timeslot, name='edit_timeslot'),
    path('timeslots/delete/<int:pk>/', views.delete_timeslot, name='delete_timeslot'),
    path('get_available_rooms', views.get_available_rooms, name='get_available_rooms'),
]
