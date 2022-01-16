# -*- coding: utf-8 -*-
from django.db import models
from user.models import Customer,Employee
from jewelry.models import Record

# Create your models here.

class Order(Record):
	'''订单.'''
	customer = models.ForeignKey(
		Customer,
		on_delete=models.PROTECT,
		blank=False,
		related_name = "order",
		verbose_name = "顾客",
	)

	other_fee = models.DecimalField("其它费用",default=0,max_digits = 10,decimal_places = 2)
	deduct = models.DecimalField("优惠金额",default=0,max_digits = 10,decimal_places = 2)

	#销售及分成
	employees = models.ManyToManyField(Employee,through='SalesShare')

	def is_balanced(self):
		return self.total_pays >= self.total_value+self.other_fee-self.deduct

	def can_close(self):
		if not self.is_payed or self.is_signed:
			return False
		else:
			for pay in self.pays:
				if pay.img is None:
					return False
		return True

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = "订单"
		verbose_name_plural = verbose_name


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
