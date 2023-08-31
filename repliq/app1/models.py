from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Company(models.Model):
    name = models.CharField(max_length=100)
   

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.CharField(max_length=254,default='email')
    phone = models.CharField(max_length=15,default='phone')
    
    

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    checked_out = models.BooleanField(default=False)
    

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField()
    returned_date = models.DateTimeField()
   
