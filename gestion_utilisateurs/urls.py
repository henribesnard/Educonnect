from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.UserProfileView.as_view(), name='edit_profile'),
    path('profil_enfant/<int:child_id>/', views.profil_enfant, name='profil_enfant'),
    path('modifier_profil_enfant/<int:child_id>/', views.modifier_profil_enfant, name='modifier_profil_enfant'),
    path('inscrire-etudiant/', views.register_student, name='register_student'),
    path('users/', views.user_list, name='user_list'),
    path('user_detail/<int:pk>/', views.user_detail_view, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/update/<int:pk>/', views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('roles/', views.role_list, name='role_list'),
    path('roles/create/', views.role_create, name='role_create'),
    path('roles/update/<int:pk>/', views.role_update, name='role_update'),
    path('roles/delete/<int:pk>/', views.role_delete, name='role_delete'),
    path('role/<int:pk>/', views.role_detail_view, name='role_detail'),
]
