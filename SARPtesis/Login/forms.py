from cProfile import label
from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'last_name', 'email', 'number', 'jobs', 'management']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'label': 'Nombre', 'placeholder': 'Nombre de Empleado'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido de Empleado'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo de Empleado'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de Empleado'}),
            'jobs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puesto de Empleado'}),
            'management': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gerencia'})
        }