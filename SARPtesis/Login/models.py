from django.db import models

# Create your models here.

# Models Questions
class Questions(models.Model):
    question = models.CharField(max_length=300)
    value = models.IntegerField(max_length=300)

# Models Evaluations
class Evaluations(models.Model):
    title = models.CharField(max_length=300)
    question = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True)

# Models department
class Department(models.Model):
    management = models.CharField(max_length=300)

    def __str__(self):
        return f'Departamento {self.management}'


# Models staff
class  Staff(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number = models.IntegerField(max_length=50)
    jobs = models.CharField(max_length=300)
    management = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'