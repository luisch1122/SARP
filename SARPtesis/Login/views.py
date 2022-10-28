from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from Login.models import Department

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

# Sign up
@login_required
def signup(request):
    if request.method == 'GET':
        return render(request, 'create_user.html', {
            'form': UserCreationForm
        })
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    )
                user.save()
                return redirect('users')

            except IntegrityError:
                return render(request, 'create_user.html', {
                    'form': UserCreationForm,
                    "error": "Username already exists"
                })

        return render(request, 'create_user.html', {
            'form': UserCreationForm,
            "error": "Password do not match"
        })

#Delete users
@login_required
def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if user:
        user.delete()
        return redirect('users')

@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

# Users edit
@login_required
def user_edit(request):

    
    return render(request, 'user_edit.html')
    # user: alberto cont: Luisch1122
        
# Home
@login_required
def home(request):
    user = request.user
    print(user)
    return render(request, 'home.html')

# Logout
def signout(request):
    logout(request)
    return redirect('login')

# Departament
@login_required
def departament(request):
    departs = Department.objects.all()
    return render(request, 'departament.html', {'departs':departs})

# staff
@login_required
def staff(request, id):
    departs = get_object_or_404(Department, pk=id)
    print(departs)
    return render(request, 'staff.html', {'departs':departs})

# evaluation
@login_required
def evaluations(request):
    return render(request, 'evaluations.html')

# users
