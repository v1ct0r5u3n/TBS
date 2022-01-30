# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator


import django_filters
from jewelry.models import Merchandise
from .models import Order,SalesShare,Refund
from django import forms

# Create your views here.

class OrderFilter(django_filters.FilterSet):
	created = django_filters.DateFromToRangeFilter(
		widget=forms.SplitDateTimeWidget(
			attrs={
				'class':'datepicker',
				'type':'date',
			}
		)
	)

	class Meta:
		model = Order
		fields = ['customer','employees','created']

class OrderListView(View):
	def get(self,request):
		ft = OrderFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'order_list.html',{'orders':page_obj,'filter':ft})
