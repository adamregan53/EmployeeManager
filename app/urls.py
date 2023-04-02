from django.contrib import admin
from django.urls import path, include, register_converter
from app import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('employees/', views.employee_list, name = 'employee_list'),
    path('employees/new/', views.employee_form, name = 'employee_new'),
    path('employees/<uuid:id>/', views.employee_form, name = 'employee_update'),
    path('search_employees', views.search_employees, name='search_employees'),
    path('employees/delete/<uuid:id>/', views.employee_delete, name = 'employee_delete'),
]