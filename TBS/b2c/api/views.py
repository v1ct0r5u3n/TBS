from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from b2c.models import Order,SalesShare,Refund

from .serializers import OrderSerializer
from .serializers import SalesShareSerializer
from .serializers import RefundSerializer
# Create your views here.

class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class SalesShareList(generics.ListCreateAPIView):
	queryset = SalesShare.objects.all()
	serializer_class = SalesShareSerializer

class SalesShareDetail(generics.RetrieveDestroyAPIView):
	queryset = SalesShare.objects.all()
	serializer_class = SalesShareSerializer

class RefundList(generics.ListCreateAPIView):
	queryset = Refund.objects.all()
	serializer_class = RefundSerializer

class RefundDetail(generics.RetrieveDestroyAPIView):
	queryset = Refund.objects.all()
	serializer_class = RefundSerializer
