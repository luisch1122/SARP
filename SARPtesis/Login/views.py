from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
def personal(request):
    return render(request, 'personal.html')

# Evaluaciones
@login_required
def evaluaciones(request):
    return render(request, 'evaluaciones.html')
