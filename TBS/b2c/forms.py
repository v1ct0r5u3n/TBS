# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Order,SalesShare,Refund
from jewelry.forms import RecordPayForm,MerchandiseRecordForm

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['customer','img','other_fee','deduct','comments']
		#exclude = ('operator','record_type','record_status','employees')


class SalesShareForm(ModelForm):
	class Meta:
		model = SalesShare
		exclude = ()


class RefundForm(ModelForm):
	class Meta:
		model= Refund
		exclude = ()


SalesShareFormSet = inlineformset_factory(	Order,
											Order.employees.through,
											form=SalesShareForm,
											fields = ['employee','share'],
											extra=1,
											can_delete=True)

RecordPayFormSet = inlineformset_factory( Order,
									Order.pays.through,
									form = RecordPayForm,
									fields = ['pay','value'],
									extra=1,
									can_delete=True)


MerchandiseRecordFormSet = inlineformset_factory(	Record,
													Record.merchandises.through,
													form = MerchandiseRecordForm,
													fields = ['package','price','comments'],
													extra = 1,
													can_delete = True,
													)