from django.urls import path
from . import views

urlpatterns = [
    path('ajouter-etablissement/', views.add_establishment, name='add_establishment'),
    path('establishments/', views.establishment_list, name='establishment_list'),
    path('establishments/<int:establishment_id>/update/', views.establishment_update, name='establishment_update'),
    path('establishments/<int:establishment_id>/delete/', views.establishment_delete, name='establishment_delete'),
    path('establishment_types/add/', views.EstablishmentTypeCreateView, name='establishment_type_add'),
    path('establishment_types/<int:pk>/edit/', views.EstablishmentTypeUpdateView, name='establishment_type_edit'),
    path('establishment_types/<int:pk>/delete/', views.EstablishmentTypeDeleteView, name='establishment_type_delete'),
    path('establishment_types/', views.EstablishmentTypeListView, name='establishment_type_list'),
]
