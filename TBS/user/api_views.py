from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Person,Employee,Customer

from .serializers import PersonSerializer
from .serializers import EmployeeSerializer
from .serializers import CustomerSerializer
# Create your views here.

class PersonList(generics.ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveDestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class EmployeeList(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
