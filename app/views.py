from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, SignUpForm
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import connection
from collections import namedtuple


# Create your views here.
def index(request):
    return render(request, "app/index.html")

def signup(request):

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:employee_list')
    
    return render(request, "registration/signup.html", {'form':form})


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "app/employee_list.html",context)


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
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            salary = request.POST.get("salary")
            position_id = request.POST.get("position")
            mobile = request.POST.get("mobile")

            cursor = connection.cursor()
            query = "INSERT INTO app_employee (first_name, last_name, salary, position_id, mobile) VALUES ('%s', '%s', '%s', '%s', '%s')" % (first_name, last_name, salary, position_id, mobile)
            cursor.executescript(query)

        return redirect('/employees/')


def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employees/')


@csrf_exempt
def search_employees(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_term = request.POST.get('searchTerm')

        #insecure implemen
        cursor = connection.cursor()
        query = "SELECT * FROM app_employee WHERE first_name LIKE '%s';" % search_term
        cursor.execute(query)
        print(cursor.fetchall())
        employees = namedtuplefetchall(cursor)

        html = render_to_string('app/search_employees.html', {'employee_list':employees})
        return HttpResponse(html)

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]