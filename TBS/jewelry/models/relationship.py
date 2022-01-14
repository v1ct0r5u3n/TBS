# -*- coding: utf-8 -*-
from django.db import models
from .merchandise import Merchandise
from core import TimeStampedMixin

class Record(models.Model,TimeStampedMixin):
	RECORD_TYPE = (
		('IN','入库单'),
		('OT','退库单'),
		('SA','销售单'),
		('SR','销售退货单'),
		('MT','维修单'),
		('MR','维修回货单'),
		('LD','借货单'),
		('LR','借货回货单'),
		('SL','拆货单'),
		('CB','组合单'),
		('TM','调货单'),
	)
	record_type = models.CharField(max_length=2,choices=Record.RECORD_TYPE)

	RECORD_STATUS_NEW = 'N'
	RECORD_STATUS_FINISHED = 'F'
	RECORD_STATUS = (
		(RECORD_STATUS_NEW,'新建'),
		(RECORD_STATUS_FINISHED,'完成'),
	)
	record_status = models.CharField(max_length=2,choices=Record.RECORD_STATUS)

	def can_close(self):
		return False

	def close(self):
		if self.can_close():
			self.record_status = RECORD_STATUS_NEW
			#self.save()

class MerchandiseRecord(models.Model):
	record = models.ForeignKey(Record,on_delete=models.CASCADE)
	merchandise = models.ForeignKey(Merchandise,on_delete=models.CASCADE)

	price = models.DecimalField("价格",default = 0,max_digits = 10,decimal_places = 2)

	to_merchandise = models.BooleanField(default=False)
	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	def __init__(self,attrs):
		if attrs is not None:
			self.attrs = attrs.copy()
		else:
			self.attrs = {}



'''
class MerchandiseRecord(models.Model):
	supplier = models.ForeignKey(
		Depot,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name = "supplies",
		verbose_name="供货商"
	)

	merchandise = models.ForeignKey()

	sku_by_supplier = models.CharField("厂家款号",max_length=20,blank=True)
	
	cost = models.DecimalField("成本",default = 0,max_digits = 10,decimal_places = 2)
	manufacture = models.CharField("产地",max_length=10,blank=True)

	class Meta:
		abstract = True


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

'''