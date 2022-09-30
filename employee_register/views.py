from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect


def employee_list(request):
    return render(request, 'employee_register/employee_list.html', {'employee_list': Employee.objects.all()})


def employee_register(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')