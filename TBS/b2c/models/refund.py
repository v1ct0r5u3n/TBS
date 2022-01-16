# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Record,MerchandiseRecord
from user.models import Customer
from core.models import Package,Pay
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

	def __str__(self):
		return str(self.id)
	class Meta:
		verbose_name = "退货"
		verbose_name_plural = verbose_name


class MerchandiseRefund(MerchandiseRecord):
	package = models.ForeignKey(Package,null = True,blank = True,on_delete = models.SET_NULL)

	def __str__(self):
		return "退货记录"
	class Meta:
		verbose_name = "退货记录"
		verbose_name_plural = verbose_name
