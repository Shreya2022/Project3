from django.db import models
from datetime import datetime

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=122,null = False)
    location = models.CharField(max_length=122)

    def __str__(self):
       return self.name

class Role(models.Model):
    name =models.CharField(max_length=122,null=False)

    def __str__(self):
       return self.name

class Employee(models.Model):
    firstname = models.CharField(max_length=122,null = False)
    lastname = models.CharField(max_length=122)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default = 0)
    bonus = models.IntegerField()
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField()
    hiredate = models.DateField()

    def __str__(self):
       return "%s %s" %(self.firstname,self.lastname)
