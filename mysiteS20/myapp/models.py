from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=200)

class Course(models.Model):
    topic=models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone=models.BooleanField(default=True)
    description=models.TextField(max_length=300, null=True, blank=True)

class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'), ('CG', 'Calgery'), ('MR', 'Montreal'), ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

class Order