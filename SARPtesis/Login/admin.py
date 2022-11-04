from tkinter import S
from django.contrib import admin
from Login.models import Staff, Department, Questions, Evaluations

# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Evaluations)
admin.site.register(Questions)