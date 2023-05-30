from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def All_emp(request):
    emps = Employee.objects.all()
    content = {
        'emps':emps
    }
    return render(request,'All_emp.html',content)

def Add_emp(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))
        role = int(request.POST.get('role'))
        dept = int(request.POST.get('dept'))
        new_emp = Employee(firstname=firstname,lastname=lastname,salary=salary,bonus=bonus,phone=phone,dept_id = dept,role_id=role,hiredate = datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    else:
      return render(request,'Add_emp.html')

def Remove_emp(request,emp_id=0):
    if emp_id:
        try:
            id_del = Employee.objects.get(id =emp_id)
            id_del.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("Please enter the valid id")
    emps = Employee.objects.all()
    Content = {
        'emps':emps
    }

    return render(request,'Remove_emp.html',Content)

def Filter_emp(request):
    if request.method=="POST":
        name = request.POST.get('name')
    
        role = request.POST.get('role')
        dept = request.POST.get('dept')
        emps = Employee.objects.all()
        
        
        if name:
            emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name))
        if role:
            emps = emps.filter(role__name = role)
        if dept:
            emps = emps.filter(dept__name = dept)

        context = {
            'emps':emps
        }
        return render(request,'All_emp.html',context)



        

    return render(request,'Filter_emp.html')
