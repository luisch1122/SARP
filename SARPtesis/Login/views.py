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

# staff
@login_required
def staff(request):
    return render(request, 'staff.html')

# evaluation
@login_required
def evaluations(request):
    return render(request, 'evaluations.html')

# users
@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

# Users edit
@login_required
def user_edit(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'GET':
        return render(request, 'user_edit.html', {'user': user})
