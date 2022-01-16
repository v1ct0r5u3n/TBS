# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record

'''
#调货单
class Transfer(Record):
	source = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return self.source.lable+'=>'+self.dest.labe

	class Meta:
		verbose_name = "调货单"
		verbose_name_plural = verbose_name

class TransferConfirm(Record):
	with_transfer = models.ForeignKey(Transfer,on_delete=models.CASCADE)
	dest = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return self.transfer.source+'=>'+self.transfer.source

	class Meta:
		verbose_name = "调货确认单"
		verbose_name_plural = verbose_name
'''