from django.shortcuts import render
from .forms import Employee

# Create your views here.


def Employee(request):
    form = Employee()
    return render(request, 'Employee.html')


def registration(request):
    return render(request, 'registration.html')
