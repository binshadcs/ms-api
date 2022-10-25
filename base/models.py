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


class Freezing_time(models.Model):
    before_t = models.TimeField()
    after_t = models.TimeField()


class Venue(models.Model):
    place = models.CharField(max_length=100)
    controller = models.CharField(max_length=100)
    cont_ph = models.IntegerField()
    cont_email = models.EmailField()
    availability = models.DateTimeField(null=True, blank=True)


class Time_set(models.Model):
    preference = models.DateTimeField()
    exclusion = models.DateTimeField()



