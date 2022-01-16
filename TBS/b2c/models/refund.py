# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Record
from .order import Order

class Refund(Record):
	with_order = models.ForeignKey(Order,on_delete = models.CASCADE,verbose_name = "订单")

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
		verbose_name = "退货"
		verbose_name_plural = verbose_name

