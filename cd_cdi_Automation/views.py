from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from cd_cdi_Automation.models import Employee
from rest_framework.response import Response
from cd_cdi_Automation.Serializers import EmployeeSerializer
from rest_framework import viewsets
from cd_cdi_Automation.forms import EmployeeForm



# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('employee-list-view')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})
