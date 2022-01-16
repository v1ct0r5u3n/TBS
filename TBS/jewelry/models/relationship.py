# -*- coding: utf-8 -*-
from django.db import models
from .merchandise import Merchandise
from core.mixins import TimeStampedMixin
from core.models import Pay,Package
from user.models import Employee

class Record(TimeStampedMixin,models.Model):
	img = models.ImageField("图像",null=True, blank=True, upload_to="transfer/")
	operator = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
	pays = models.ManyToManyField(Pay,through='RecordPay')
	comments = models.TextField("备注",blank = True,max_length=100)
	'''
	RECORD_TYPE_IN = 'IN'
	RECORD_TYPE_OUT = 'OT'
	RECORD_TYPE_SALE = 'SA'
	RECORD_TYPE_REFUND = 'SR'
	RECORD_TYPE_MAINTAIN = 'MT'
	RECORD_TYPE_MAINTAIN_RETURN = 'MR'
	RECORD_TYPE_LEND = 'LD'
	RECORD_TYPE_LEND_RETURN = 'LR'
	RECORD_TYPE_TRANSFORM = 'TM'
	RECORD_TYPE_DISASSEMBLE = 'DA'
	RECORD_TYPE_ASSEMBLE = 'AS'
	
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
		(RECORD_TYPE_DISASSEMBLE,'拆分单'),
		(RECORD_TYPE_ASSEMBLE,'组合单'),
	)
	record_type = models.CharField(max_length=2,choices=RECORD_TYPE)
	'''
	RECORD_STATUS_NEW = 'N'
	RECORD_STATUS_FINISHED = 'F'
	RECORD_STATUS = (
		(RECORD_STATUS_NEW,'新建'),
		(RECORD_STATUS_FINISHED,'完成'),
	)
	record_status = models.CharField(max_length=2,choices=RECORD_STATUS)

	@property
	def total_price(self):
		return sum(merchandise.price for mechandise in self.merchandises)

	@property
	def total_value(self):
		return sum(merchandiseorder.actrual_price for merchandiseorder in self.merchandiseorder_set)

	@property
	def total_pays(self):
		return sum(recordpay.value for recordpay in self.orderpay_set)

	@property
	def is_shipped(self):
		for merchandise in self.merchandises:
			if merchandise.package is None:
				return False
		return True

	@property
	def is_signed(self):
		for merchandise in self.merchandises:
			if not mechandise.package or not mechandise.package.is_signed:
				return False
		return True

	def is_balanced(self):
		return self.total_pays >= self.total_value

	def can_close(self):
		return False

	def close(self):
		if self.can_close():
			self.record_status = RECORD_STATUS_NEW
			#self.save()

class MerchandiseRecord(models.Model):
	record = models.ForeignKey(Record,on_delete=models.CASCADE)
	merchandise = models.ForeignKey(Merchandise,on_delete=models.CASCADE)

	package = models.ForeignKey(Package,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='包裹')
	price = models.DecimalField("价格",default = 0,max_digits = 10,decimal_places = 2)

	#Q:Can we assume record implies the direction
	#A:Needed by assemble,which is merchandise(s)=>merchandise,or in disassemble vice versa.
	to_merchandise = models.BooleanField(default=False)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

class RecordPay(models.Model):
	pay = models.ForeignKey(Pay,on_delete=models.CASCADE)
	record = models.ForeignKey(Record,on_delete=models.CASCADE)

	value = models.DecimalField(max_digits = 10,decimal_places = 2)

