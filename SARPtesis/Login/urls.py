from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('home/', views.home, name="index"),
    path('logout/', views.signout, name='logout'),
    path('personal/', views.staff, name='staff'),
    path('personal/editar/<int:id>', views.user_edit, name='user_edit'),
    path('evaluaciones/', views.evaluations, name='evaluations'),
    path('usuarios/', views.users, name='users')
]