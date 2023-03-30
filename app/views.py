from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, SignUpForm
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import connection
from collections import namedtuple


# Create your views here.
def index(request):
    return render(request, "app/index.html")

def signup(request):
    if request.user.is_superuser:
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('app:employee_list')
        
        return render(request, "registration/signup.html", {'form':form})
    
    else:
        return redirect('login')

@login_required
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "app/employee_list.html",context)

@login_required
def employee_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance = employee)
        return render(request, "app/employee_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)

        if form.is_valid():
            form.save()

        return redirect('/employees/')

@login_required
def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employees/')

@login_required
@csrf_exempt
def search_employees(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_term = request.POST.get('searchTerm')
        employees = Employee.objects.filter(first_name__icontains = search_term)

        html = render_to_string('app/search_employees.html', {'employee_list':employees})
        return HttpResponse(html)
