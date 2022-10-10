from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

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
    
def home(request):
    user = request.user
    if user == None:
        return redirect('login')
    else:
        return render(request, 'home.html')