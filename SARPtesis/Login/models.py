from django.db import models

# Create your models here.



    
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
    number = models.IntegerField()
    jobs = models.CharField(max_length=300)
    management = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


# Models Evaluations
class Evaluation(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True)
    complete = models.BooleanField(null=True)
    department = models.ForeignKey(Department(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'

# Models Questions
class Questions(models.Model):
    question = models.CharField(max_length=300)
    value = models.IntegerField()
    evaluations = models.ForeignKey(Evaluation, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'Pregunta {self.question} Valor {self.value} Evaluacion {self.evaluations}'