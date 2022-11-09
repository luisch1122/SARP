from django import forms
from .models import Staff, Evaluation, Questions

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'last_name', 'email', 'number', 'jobs', 'management']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'number': 'Numero',
            'jobs': 'Puesto',
            'management': 'Departamento'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Empleado'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido de Empleado'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo de Empleado'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de Empleado'}),
            'jobs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puesto de Empleado'}),
            'management': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gerencia'})
        }

class EvalForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['title', 'description', 'department']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la evaluación'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribir descripción'})
        }

class QuestForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'value']
        label = ['Preguntas', 'Valor']
        widgets ={
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese pregunta'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'})   
        }