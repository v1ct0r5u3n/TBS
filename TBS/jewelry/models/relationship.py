# -*- coding: utf-8 -*-
from django.db import models
from .merchandise import Merchandise
from core.mixins import TimeStampedMixin
from core.models import Pay
from user.models import Employee

class Record(TimeStampedMixin,models.Model):
	operator = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
	pays = models.ManyToManyField(Pay,through='RecordPay')

	RECORD_TYPE_IN = 'IN'
	RECORD_TYPE_OUT = 'OT'
	RECORD_TYPE_SALE = 'SA'
	RECORD_TYPE_REFUND = 'SR'
	RECORD_TYPE_MAINTAIN = 'MT'
	RECORD_TYPE_MAINTAIN_RETURN = 'MR'
	RECORD_TYPE_LEND = 'LD'
	RECORD_TYPE_LEND_RETURN = 'LR'
	RECORD_TYPE_TRANSFORM = 'TM'
	RECORD_TYPE_REMAKE = 'RM'
	RECORD_TYPE_COMPOSE = 'CP'
	
	RECORD_TYPE = (
		(RECORD_TYPE_IN,'入库单'),
		(RECORD_TYPE_OUT,'退库单'),
		(RECORD_TYPE_SALE,'销售单'),
		(RECORD_TYPE_REFUND,'销售退货单'),
		(RECORD_TYPE_MAINTAIN,'维修单'),
		(RECORD_TYPE_MAINTAIN_RETURN,'维修回货单'),
		(RECORD_TYPE_LEND,'借货单'),
		(RECORD_TYPE_LEND_RETURN,'借货回货单'),
		(RECORD_TYPE_TRANSFORM,'调货单'),
		(RECORD_TYPE_REMAKE,'拆分单'),
		(RECORD_TYPE_COMPOSE,'组合单'),
	)
	record_type = models.CharField(max_length=2,choices=RECORD_TYPE)

	RECORD_STATUS_NEW = 'N'
	RECORD_STATUS_FINISHED = 'F'
	RECORD_STATUS = (
		(RECORD_STATUS_NEW,'新建'),
		(RECORD_STATUS_FINISHED,'完成'),
	)
	record_status = models.CharField(max_length=2,choices=RECORD_STATUS)

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

class RecordPay(models.Model):
	pay = models.ForeignKey(Pay,on_delete=models.CASCADE)
	record = models.ForeignKey(Record,on_delete=models.CASCADE)

	value = models.DecimalField(max_digits = 10,decimal_places = 2)


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