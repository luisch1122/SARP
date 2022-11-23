from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('home/', views.home, name="index"),
    path('logout/', views.signout, name='logout'),
    path('departamento/', views.departament, name='departament'),
    path('departamento/personal/<int:id>', views.staff, name='staff'),
    path('departamento/personal/crear', views.create_staff, name='create_staff'),
    path('departamento/personal/<int:id>/edit', views.edit_staff, name='edit_staff'),
    path('departamento/personal/<int:id>/delete', views.delete_staff, name='delete_staff'),
    # path('personal/editar/<int:id>', views.user_edit, name='user_edit'),
    path('evaluaciones/', views.evaluations, name='evaluations'),
    path('evaluaciones/crear', views.create_evaluation, name='create_evaluation'),
    path('evaluaciones/<int:id>/crear_preguntas', views.create_question, name='create_question'),
    path('evaluaciones/<int:id>/eliminar', views.delete_evaluation, name='delete_evaluation'),
    path('evaluaciones/<int:id>/answer', views.answer, name='answer'),
    path('evaluaciones/answer/<int:id>/test/<int:id_staff>', views.test, name='test'),
    path('usuarios/', views.users, name='users'),
    path('usuarios/crear', views.signup, name='sign_up'), 
    path('usarios/<int:id>/delete', views.delete_user, name='delete_user'),
]