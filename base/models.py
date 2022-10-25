from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Department(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    hod_email = models.EmailField()
    hod_ph = models.IntegerField()



