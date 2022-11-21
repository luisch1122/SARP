from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from Login.models import Department, Staff, Evaluation, Questions, Answers
from .forms import StaffForm, EvalForm, QuestForm

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
            'error': 'Usuario o Contraseña incorrecta'
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
                    "error": "Usuario ya existe"
                })

        return render(request, 'create_user.html', {
            'form': UserCreationForm,
            "error": "Las contraseñas no son iguales"
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
    staff = Staff.objects.filter(management = id)
    print(staff)
    return render(request, 'staff.html', {'departs':departs, 'staffs':staff})

# Create staff
@login_required
def create_staff(request):
    if request.method == 'GET':
        return render(request, 'create_staff.html', {'form':StaffForm})
    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departament')

# Edit Staff
@login_required
def edit_staff(request, id):
    if request.method == 'GET':
        staff = get_object_or_404(Staff, pk=id)
        form = StaffForm(instance=staff)
        return render(request, 'create_staff.html', {'form':form})
    else:
        staff = get_object_or_404(Staff, pk=id)
        form = StaffForm(request.POST, instance=staff)
        form.save()
        return redirect('departament')

#Delete staff
@login_required
def delete_staff(request, id):
    staff = get_object_or_404(Staff, pk=id)
    if staff:
        staff.delete()
        return redirect('departament')

# evaluation
@login_required
def evaluations(request):
    eval = Evaluation.objects.all()
    return render(request, 'evaluations.html', {'evals': eval})

# Create evaluation
@login_required
def create_evaluation(request):
    if request.method == 'GET':
        return render(request, 'create_evaluation.html', {'form':EvalForm})
    else:
        form = EvalForm(request.POST)
        form.save()
        return redirect('evaluations')

# Delete evaluation
@login_required
def delete_evaluation(request, id):
    eval = get_object_or_404(Evaluation, pk=id)
    if eval:
        eval.delete()
        return redirect('evaluations')

# Create question
@login_required
def create_question(request, id):
    if request.method == 'GET':   
        return render(request, 'create_question.html', {'form':QuestForm(), 'id':id})
    else:
        print('valor:', request.POST)
        quest = Questions.objects.create(
            question=request.POST['question'],
            value=request.POST['value'],
        )
        instance = quest
        instance.evaluations = Evaluation(id)
        instance.save()
        return redirect('evaluations')

# answer
@login_required
def answer(request, id):
    eval = Evaluation.objects.get(pk=id)
    depart = eval.department.id
    staff = Staff.objects.filter(management = depart)
    return render(request, 'answer.html', {'staffs':staff, 'eval':eval})

# List Test
@login_required
def test(request, id):
    eval = Evaluation.objects.get(pk=id)
    quest = Questions.objects.filter(evaluations = id)
    answer = Answers.objects.all()

    if request.method == 'GET':
        return render(request, 'test.html', {'eval':eval, 'quests':quest, 'answers':answer})
    else: 
        print(request.POST['quests'])
        resul = request.POST
        res = list(resul.values())
        print(res)
        return redirect('evaluations')