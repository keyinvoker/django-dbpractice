from django.db import models
from datetime import datetime

# Create your models here.
class People(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    income = models.IntegerField()
    password = models.CharField(max_length=500)
    updated = models.BooleanField(default=False)
    