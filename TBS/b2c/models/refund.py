# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Record,MerchandiseRecord
from user.models import Customer
from core.models import Package
from core.mixins import TimeStampedMixin

class Refund(Record):
	customer = models.ForeignKey(
		Customer,
		null = True,
		blank = True,
		on_delete = models.SET_NULL,
		related_name = "refund_record",
		verbose_name = "顾客"
	)

	actrual_price = models.DecimalField("退款金额",default = 0,max_digits = 10,decimal_places = 2)

	def __str__(self):
		return str(self.order_id)
	class Meta:
		verbose_name = "退款"
		verbose_name_plural = verbose_name


class MechandiseRefund(MerchandiseRecord):
	package = models.ForeignKey(
		Package,
		null = True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name = "refund_record",
		verbose_name = "包裹"
	)

	def __str__(self):
		return "退货记录"
	class Meta:
		verbose_name = "退货记录"
		verbose_name_plural = verbose_name
