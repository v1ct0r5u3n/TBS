from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Package
from .models import Area,Address
from .models import Pay

from .serializers import PackageSerializer
from .serializers import AreaSerializer
from .serializers import AddressSerializer
from .serializers import PaySerializer
# Create your views here.

class PackageList(generics.ListCreateAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageSerializer

class PackageDetail(generics.RetrieveDestroyAPIView):
	queryset = Package.objects.all()
	serializer_class = PackageSerializer

class AreaList(generics.ListCreateAPIView):
	queryset = Area.objects.all()
	serializer_class = AreaSerializer

class AreaDetail(generics.RetrieveDestroyAPIView):
	queryset = Area.objects.all()
	serializer_class = AreaSerializer

class AddressList(generics.ListCreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveDestroyAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class PayList(generics.ListCreateAPIView):
	queryset = Pay.objects.all()
	serializer_class = PaySerializer

class PayDetail(generics.RetrieveDestroyAPIView):
	queryset = Pay.objects.all()
	serializer_class = PaySerializer
