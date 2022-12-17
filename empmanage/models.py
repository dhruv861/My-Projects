#from django.db import models
from django.db import models

# Create your models here.

class Details(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    #working=models.BooleanField()
    department=models.CharField(max_length=20)
    