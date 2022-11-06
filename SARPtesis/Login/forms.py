from django import forms
from .models import Staff, Evaluation, Questions

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'last_name', 'email', 'number', 'jobs', 'management']
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
        fields = ['title', 'complete']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la evaluación'})
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