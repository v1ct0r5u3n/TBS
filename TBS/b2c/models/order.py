# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone
from user.models import Person,Customer,Employee
from jewelry.models import Record,MerchandiseRecord,Merchandise,Depot
#from computedfields.models import ComputedFieldsModel, computed
from core.models import Package
from core.mixins import TimeStampedMixin

# Create your models here.

class Order(Record):
	'''订单.'''
	order_id = models.BigAutoField("订单号",primary_key=True)
	customer = models.ForeignKey(
		Customer,
		on_delete=models.PROTECT,
		blank=False,
		related_name = "order",
		verbose_name = "顾客",
	)

	employees = models.ManyToManyField(
		Employee,
		through='SalesShare',
	)
	
	other_fee = models.DecimalField("其它费用",default=0,max_digits = 10,decimal_places = 2)
	deduct = models.DecimalField("优惠金额",default=0,max_digits = 10,decimal_places = 2)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	@property
	def total_price(self):
		return sum(merchandise.price for mechandise in self.merchandises)

	@property
	def total_value(self):
		return sum(merchandiseorder.actrual_price for merchandiseorder in self.merchandiseorder_set)+other_fee-deduct

	@property
	def total_deduct(self):
		return self.total_value-self.total_price

	@property
	def total_pays(self):
		return sum(pay.value for pay in self.pays)

	@property
	def is_payed(self):
		return self.total_pays >= self.total_value

	@property
	def is_shipped(self):
		for mechandise in self.merchandises:
			if mechandise.package is None:
				return False
		return True

	@property
	def is_signed(self):
		for mechandise in self.merchandises:
			if not mechandise.package or not mechandise.package.is_signed:
				return False
		return True

	def can_close(self):
		if not self.is_payed or self.is_signed:
			return False
		else:
			for pay in self.pays:
				if pay.img is None:
					return False
		return True

	def __str__(self):
		return str(self.order_id)

	class Meta:
		verbose_name = "订单"
		verbose_name_plural = verbose_name

class MerchandiseOrder(MerchandiseRecord):
	package = models.ForeignKey(
		Package,
		null = True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name = "sales_record",
		verbose_name = "包裹"
	)
	actrual_price = models.DecimalField("售价",default = 0,max_digits = 10,decimal_places = 2)
	def __init__(self,attrs = None):
		to_merchandise = {'to_merchandise':False}
		if attrs is None:
			attrs = to_merchandise
		else:
			attrs.update(to_merchandise)

		super(MerchandiseOrder,self).__init__(self,attrs)

#销售分成
class SalesShare(models.Model):
	order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		related_name="sales_share",
		verbose_name="订单"
	)
	employee = models.ForeignKey(
		Employee,
		on_delete=models.CASCADE,
		related_name="sales_share",
		verbose_name="销售"
	)
	share = models.DecimalField(r"销售分成(%)",max_digits = 4,decimal_places = 1)

	def __str__(self):
		return str(self.employee)+":"+str(self.share)+r"%"

	class Meta:
		verbose_name = "销售分成"
		verbose_name_plural = verbose_name

def AddMerchandiseToOrder(merchandises,order):
	return

