from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from b2b.models import B2BRecord,B2BConfirm


from .serializers import B2BRecordSerializer
from .serializers import B2BConfirmSerializer
# Create your views here.

class B2BRecordList(generics.ListCreateAPIView):
	queryset = B2BRecord.objects.all()
	serializer_class = B2BRecordSerializer

class B2BRecordDetail(generics.RetrieveDestroyAPIView):
	queryset = B2BRecord.objects.all()
	serializer_class = B2BRecordSerializer

class B2BConfirmList(generics.ListCreateAPIView):
	queryset = B2BConfirm.objects.all()
	serializer_class = B2BConfirmSerializer

class B2BConfirmDetail(generics.RetrieveDestroyAPIView):
	queryset = B2BConfirm.objects.all()
	serializer_class = B2BConfirmSerializer
