from django.db import models
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from .filters import MerchandiseFilter,OtherFilter,JewelFilter,AccessoryFilter,PearlFilter,DiamondFilter,ColoredGemFilter



# Create your views here.
class JewelryListView(View):
	def get(self,request):
		ft = MerchandiseFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'merchandise_list.html',{'merchandises':page_obj,'filter':ft})

class JewelListView(View):
	def get(self,request):
		ft = JewelFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'jewel_list.html',{'merchandises':page_obj,'filter':ft})

class AccessoryListView(View):
	def get(self,request):
		ft = AccessoryFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'accessory_list.html',{'merchandises':page_obj,'filter':ft})


class PearlListView(View):
	def get(self,request):
		ft = PearlFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'pearl_list.html',{'merchandises':page_obj,'filter':ft})


class DiamondListView(View):
	def get(self,request):
		ft = DiamondFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'diamond_list.html',{'merchandises':page_obj,'filter':ft})


class ColoredGemListView(View):
	def get(self,request):
		ft = ColoredGemFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'colored_gem_list.html',{'merchandises':page_obj,'filter':ft})

class OtherListView(View):
	def get(self,request):
		ft = OtherFilter(request.GET)
		merchandises = ft.qs
		paginator = Paginator(merchandises, 15)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'other_list.html',{'merchandises':page_obj,'filter':ft})