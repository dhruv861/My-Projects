from cmath import e
from pickle import NONE
from django.shortcuts import render,redirect
from empmanage.models import Details
from django.urls import reverse
#from django.http import HttpResponse

# Create your views here.


def home(request):
    emp=Details.objects.all().values()
   # emp=list(enumerate(emp,1))

    return render(request,"empmanage/home.html",{'emps':emp})

def addEmployee(request):
    if request.method =="POST":
        emp=request.POST
        print(emp['email'],type(emp))

        e=Details()
        e.name=emp['emp_name']
        e.emp_id=emp['emp_id']
        e.email=emp.__getitem__('email')
        e.phone=emp.__getitem__('phone')
        e.address=emp.__getitem__('address')
        e.department=emp.__getitem__('department')
        
        e.save()
        return redirect(reverse('emphome'))

    return render(request,"empmanage/AddEmployee.html")

def delete_emp(request,emp_id):
        emp=Details.objects.get(pk=emp_id)
        print(emp_id)
        emp.delete()
        return redirect(reverse('emphome'))

def update_emp(request,emp_id):
        
    emp=Details.objects.get(pk=emp_id)
    print(emp)
    context={'emp':emp}
    if request.method == 'POST':
            
        emp=request.POST
        print(emp['email'],type(emp))

        e=Details.objects.get(pk=emp_id)
        e.name=emp['emp_name']
        e.emp_id=emp['emp_id']
        e.email=emp.__getitem__('email')
        e.phone=emp.__getitem__('phone')
        e.address=emp.__getitem__('address')
        e.department=emp.__getitem__('department')
        
        e.save()
        return redirect(reverse('emphome'))

        
    return render(request,'empmanage/UpdateEmployee.html',context)

    