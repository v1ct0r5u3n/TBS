# -*- coding: utf-8 -*-
from django.db import models


#调货单
class Transfer(models.Model):
	datetime = models.DateTimeField("付款时间",default = timezone.now)
	merchandise = models.ManyToManyField(Merchandise)
	source = models.ForeignKey(
		Depot,
		on_delete=models.PROTECT,
		blank=False,
		related_name = "+",
	)
	destination = models.ForeignKey(
		Depot,
		on_delete=models.PROTECT,
		blank=False,
		related_name = "+",
	)

	def __str__(self):
		return source.lable+"->"+destination.lable+":"+str(merchandise.objects.count())

	class Meta:
		verbose_name = "调货单"
		verbose_name_plural = verbose_name


#借货单
class Lend(models.Model):
	pass

#加工单
class Maintain(models.Model):
	pass

#盘点单
class StockTake(models.Model):
	pass