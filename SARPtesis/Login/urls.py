from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('home/', views.home, name="index"),
    path('logout/', views.signout, name='logout'),
    path('departamento/', views.departament, name='departament'),
    path('departamento/personal/<int:id>', views.staff, name='staff'),
    # path('personal/editar/<int:id>', views.user_edit, name='user_edit'),
    path('evaluaciones/', views.evaluations, name='evaluations'),
    path('usuarios/', views.users, name='users'),
    path('usuarios/crear', views.signup, name='sign_up'), 
    path('usarios/<int:id>/delete', views.delete_user, name='delete_user'),
]