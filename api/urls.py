from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),#getdata about geting department detiles from model
    path('addDep',views.addDepartment),
]