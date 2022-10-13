from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="login"),
    path('home/', views.home, name="index"),
    path('logout/', views.signout, name='logout'),
    path('personal/', views.personal, name='personal'),
    path('evaluaciones/', views.evaluaciones, name='evaluaciones')
]