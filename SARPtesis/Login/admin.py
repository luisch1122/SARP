from tkinter import S
from django.contrib import admin
from Login.models import Staff, Department, Questions, Evaluation, Answers

# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Evaluation)
admin.site.register(Questions)
admin.site.register(Answers)