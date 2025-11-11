from django.shortcuts import render
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework import generics
# Create your views here.


class Employeecreateview(generics.ListCreateAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer

class Employeecrudview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

