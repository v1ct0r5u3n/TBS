# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator


import django_filters
from jewelry.models import Merchandise
from .models import Order,SalesShare,Refund
from django import forms
from django.views.generic.edit import CreateView,UpdateView


from .forms import OrderForm,SalesShareForm,RefundForm,SalesShareFormSet,RecordPayFormSet,MerchandiseRecordFormSet

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

		return render(request,'b2c/order_list.html',{'orders':page_obj,'filter':ft})


class OrderDetailView(DetailView):
	model = Order
	fields = '__all__'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		self.order = get_object_or_404(Order, pk=self.kwargs['pk'])
		context['customer'] = self.order.customer

		return context


class CreateOrderView(CreateView):
	form_class = OrderForm
	template_name = 'b2c/order_form.html'
	#fields = '__all__'

	def get_context_data(self, **kwargs):
		data = super(CreateOrderView, self).get_context_data(**kwargs)
		if self.request.POST:
			data['merchandises'] = MerchandiseRecordFormSet(self.request.POST)
			data['sales_share'] = SalesShareFormSet(self.request.POST)
			data['record_pays'] = RecordPayFormSet(self.request.POST)
		else:
			data['merchandises'] = MerchandiseRecordFormSet()
			data['sales_share'] = SalesShareFormSet(initial=[{'employee':self.request.user,'share':100}])
			data['record_pays'] = RecordPayFormSet()
		return data

	def form_valid(self, form):
		context = self.get_context_data(form=form)
		merchandises = context['merchandises']
		sales_share = context['sales_share']
		record_pays = context['record_pays']
		with transaction.commit_on_success():
			form.instance.operator = self.request.user
			form.instance.record_type = RECORD_TYPE_B2C_SALE
			form.instance.record_status = RECORD_STATUS_NEW
			self.object = form.save()

		if merchandises.is_valid():
			merchandises.instance = self.object
			merchandises.save()

		if sales_share.is_valid():
			sales_share.instance = self.object
			sales_share.save()

		if record_pays.is_valid():
			record_pays.instance = self.object
			record_pays.save()

		return super(CreateOrderView, self).form_valid(form)

	def get_success_url(self):
		return reverse('order_list')

class UpdateOrderView(UpdateView):
	form_class = OrderForm
	template_name = 'b2c/order_form.html'
	#fields = '__all__'

	def get_context_data(self, **kwargs):
		data = super(CreateOrderView, self).get_context_data(**kwargs)
		if self.request.POST:
			data['sales_share'] = SalesShareFormSet(self.request.POST,instance=self.object)
			data['sales_share'].full_clean()
			data['record_pays'] = RecordPayFormSet(self.request.POST,instance=self.object)
			data['record_pays'].full_clean()
		else:
			data['sales_share'] = SalesShareFormSet(instance=self.object)
			data['record_pays'] = RecordPayFormSet(instance=self.object)
		return data

	def form_valid(self, form):
		context = self.get_context_data(form=form)
		sales_share = context['sales_share']
		record_pays = context['record_pays']
		with transaction.commit_on_success():
			form.instance.operator = self.request.user
			self.object = form.save()
		if sales_share.is_valid():
			sales_share.instance = self.object
			sales_share.save()

		if record_pays.is_valid():
			record_pays.instance = self.object
			record_pays.save()

		return super(CreateOrderView, self).form_valid(form)

	def get_success_url(self):
		return reverse('order_list')





