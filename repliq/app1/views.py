from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, SetPasswordForm
from . forms import usercf,CompanyForm, EmployeeForm, DeviceForm, DeviceLogForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Company, Employee, Device, DeviceLog




# user creation/ registration
def usercform(request):
    if request.method == "POST":
        frm = usercf(request.POST)
        if frm.is_valid():
            messages.success(request, 'Succesfully Registerd!')
            frm.save()
            
    else:
        frm = usercf()
    return render(request, 'app1/usercform.html', {'form':frm})


#login 


def login_form(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request,data= request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upass = frm.cleaned_data['password']
            user = authenticate(username = uname,password = upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/success')
    else:        
        frm = AuthenticationForm()
    return render(request,'app1/login.html',{'form':frm})





#Logout
def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')


def userCform(request):
    if request.method == 'POST':
        frm = usercf(request.POST)
        if frm.is_valid():
            frm.save()
    else:        
        frm = usercf()
    return render(request,'app1/usercform.html',{'form':frm})



#successfully login 
@login_required(login_url='login')
def slogin(request):
     return render(request,'app1/success.html')




def company_list(request):
    companies = Company.objects.all()
    return render(request, 'app1/company_list.html', {'companies': companies})

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'app1/add_company.html', {'form': form})


def showe(request):
    x = Employee.objects.all()
    return render(request, 'app1/employee.html', {'form': x})


def adde(request):
    if request.method == 'POST':
        frm = EmployeeForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/success/')
    else:        
        frm = EmployeeForm()
    return render(request,'app1/add_company.html',{'form':frm})



