# -*- coding: utf-8 -*-
from django.db import models
from .merchandise import Merchandise
from core.mixins import TimeStampedMixin,ThumbnailMixin,OperatorMixin
from core.models import Pay,Package
from user.models import Employee

class Record(	TimeStampedMixin,
				ThumbnailMixin,
				OperatorMixin,
				models.Model):
	pays = models.ManyToManyField(Pay,through='RecordPay')
	comments = models.TextField("备注",blank = True,max_length=100)
	
	RECORD_TYPE_B2C_SALE = 'CSA'
	RECORD_TYPE_B2C_REFUND = 'CSR'
	RECORD_TYPE_B2C_REPAIR = 'CRP'
	RECORD_TYPE_B2C_REPAIR_RETURN = 'CRR'
	RECORD_TYPE_B2B_IN = 'BIN'
	RECORD_TYPE_B2B_OUT = 'BOT'
	RECORD_TYPE_B2B_REPAIR = 'BRP'
	RECORD_TYPE_B2B_REPAIR_RETURN = 'BRR'
	RECORD_TYPE_B2B_LEND = 'BLD'
	RECORD_TYPE_B2B_LEND_RETURN = 'BLR'
	RECORD_TYPE_B2B_TRANSFER = 'BTF'
	RECORD_TYPE_B2B_TRANSFER_CONFIRM = 'BTC'
	RECORD_TYPE_B2B_DISASSEMBLE = 'BDA'
	RECORD_TYPE_B2B_ASSEMBLE = 'BAS'
	
	RECORD_TYPE = (
		(RECORD_TYPE_B2C_SALE,'销售单'),
		(RECORD_TYPE_B2C_REFUND,'销售退货单'),
		(RECORD_TYPE_B2C_REPAIR,'客户维修单'),
		(RECORD_TYPE_B2C_REPAIR_RETURN,'客户维修返回单'),
		(RECORD_TYPE_B2B_IN,'入库单'),
		(RECORD_TYPE_B2B_OUT,'退库单'),
		(RECORD_TYPE_B2B_REPAIR,'维修单'),
		(RECORD_TYPE_B2B_REPAIR_RETURN,'维修回货单'),
		(RECORD_TYPE_B2B_LEND,'借货单'),
		(RECORD_TYPE_B2B_LEND_RETURN,'借货回货单'),
		(RECORD_TYPE_B2B_TRANSFER,'调货单'),
		(RECORD_TYPE_B2B_TRANSFER_CONFIRM,'调货确认单'),
		(RECORD_TYPE_B2B_DISASSEMBLE,'拆分单'),
		(RECORD_TYPE_B2B_ASSEMBLE,'组装单'),
	)
	record_type = models.CharField(max_length=3,choices=RECORD_TYPE)
	
	RECORD_STATUS_NEW = 'N'
	RECORD_STATUS_FINISHED = 'F'
	RECORD_STATUS = (
		(RECORD_STATUS_NEW,'新建'),
		(RECORD_STATUS_FINISHED,'完成'),
	)
	record_status = models.CharField(max_length=2,choices=RECORD_STATUS)

	@property
	def total_count_of_merchandise(self):
		return self.merchandises.count

	@property
	def total_price(self):
		return sum(merchandise.price for merchandise in self.merchandises.all())

	@property
	def total_value(self):
		return sum(merchandiserecord.price for merchandiserecord in self.merchandiserecord_set.all())

	@property
	def total_count_of_pays(self):
		return self.recordpay_set.count

	@property
	def total_pays(self):
		return sum(recordpay.value for recordpay in self.recordpay_set.all())

	@property
	def total_unpay(self):
		return self.total_value-self.total_pays

	@property
	def total_count_of_packages(self):
		packages = set()
		for merchandise in self.merchandises.all():
			if merchandise.package is not None:
				package.add(merchandise.package)

		return len(packages)


	@property
	def is_shipped(self):
		for merchandiserecord in self.merchandiserecord_set.all():
			if merchandiserecord.package is None:
				return False
			if merchandiserecord.package.ship_date is None:
				return False
		return True

	@property
	def is_signed(self):
		for merchandiserecord in self.merchandiserecord_set.all():
			if not merchandiserecord.package or not merchandiserecord.package.is_signed:
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

	class Meta:
		verbose_name = "操作记录"
		verbose_name_plural = verbose_name

class MerchandiseRecord(models.Model):
	record = models.ForeignKey(Record,on_delete=models.CASCADE)
	merchandise = models.ForeignKey(Merchandise,on_delete=models.CASCADE)

	package = models.ForeignKey(Package,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='包裹')
	price = models.DecimalField("价格",default = 0,max_digits = 10,decimal_places = 2)

	#Q:Can we assume record implies the direction
	#A:Needed by assemble,which is merchandise(s)=>merchandise,or in disassemble vice versa.
	to_merchandise = models.BooleanField(default=False)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	class Meta:
		verbose_name = "商品操作记录"
		verbose_name_plural = verbose_name

class RecordPay(models.Model):
	pay = models.ForeignKey(Pay,on_delete=models.CASCADE)
	record = models.ForeignKey(Record,on_delete=models.CASCADE)

	value = models.DecimalField(max_digits = 10,decimal_places = 2)
	class Meta:
		verbose_name = "付款记录"
		verbose_name_plural = verbose_name





