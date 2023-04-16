from django.urls import path
from . import views

urlpatterns = [
    path('events/add/', views.add_event, name='add_event'),
    path('events/', views.events_list, name='events_list'),
    path('events/<int:pk>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
]
