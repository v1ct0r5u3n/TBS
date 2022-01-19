from rest_framework import serializers
from .models import Person,Employee,Customer

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'
