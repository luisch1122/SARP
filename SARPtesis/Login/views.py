from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Login
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usernamer or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('index')
    
# Home
@login_required
def home(request):
    return render(request, 'home.html')

# Logout
def signout(request):
    logout(request)
    return redirect('login')

# Personal
@login_required
def staff(request):
    return render(request, 'staff.html')

# Evaluaciones
@login_required
def evaluations(request):
    return render(request, 'evaluations.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
