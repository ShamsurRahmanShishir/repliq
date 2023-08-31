from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company, Employee, Device, DeviceLog

class usercf(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'company','email','phone']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'condition']

class DeviceLogForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['device', 'employee', 'checked_out_date', 'returned_date']
