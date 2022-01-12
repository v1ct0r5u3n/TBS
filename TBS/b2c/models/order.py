# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone
from user.models import Person,Address,Customer,Employee
from jewelry.models import Merchandise,Depot
from computedfields.models import ComputedFieldsModel, computed

# Create your models here.

class Order(models.Model):
	'''订单.'''
	order_id = models.BigAutoField("订单号",primary_key=True)
	customer = models.ForeignKey(
		Customer,
		on_delete=models.PROTECT,
		blank=False,
		related_name = "order",
		verbose_name = "顾客",
	)

	order_date = models.DateTimeField("订单日期",default=timezone.now)
	last_change = models.DateTimeField('最后修改',default=timezone.now)
	
	other_fee = models.DecimalField("其它",default=0,max_digits = 10,decimal_places = 2)
	deduct = models.DecimalField("优惠金额",default=0,max_digits = 10,decimal_places = 2)
	total_value = models.DecimalField("总价",max_digits = 10,decimal_places = 2)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	is_payed = models.BooleanField("付款",default = False)
	is_shiped = models.BooleanField("发货",default = False)
	is_recieved = models.BooleanField("签收",default = False)

	def __str__(self):
		return str(self.order_id)
	class Meta:
		verbose_name = "订单"
		verbose_name_plural = verbose_name

class Package(models.Model):
	ship_date = models.DateTimeField("发货日期",null = True,blank = True)
	sign_date = models.DateTimeField("签收日期",null=True,blank = True)

	carrier = models.CharField("承运",blank=True,default="自提",max_length=20)
	track_no = models.CharField("运单号",blank = True,default = "",max_length=20)
	gross_weight = models.FloatField("毛重",default=0)

	ship_fee = models.DecimalField("运费",default=0,max_digits = 10,decimal_places = 2)
	packaging = models.DecimalField("包装费",default=0,max_digits = 10,decimal_places = 2)
	insurance = models.DecimalField("保险",default=0,max_digits = 10,decimal_places = 2)
	other_fee = models.DecimalField("其它",default=0,max_digits = 10,decimal_places = 2)

	def __str__(self):
		return "包裹"
	class Meta:
		verbose_name = "包裹"
		verbose_name_plural = verbose_name

class SalesRecord(ComputedFieldsModel):
	merchandise = models.ForeignKey(
		Merchandise,
		null = True,
		blank = False,
		on_delete=models.SET_NULL,
		related_name = "sales_record",
		verbose_name = "商品"
	)
	
	#简单记录商品信息，一旦商品删除后销售记录仍然可查询
	#description = models.CharField("商品描述",max_length=100)
	#price = models.FloatField("标价",default=0)
	@computed(models.CharField("商品描述",max_length=100), depends=[['merchandise', ['description']]])
	def description(self):
		return self.merchandise.description if(self.merchandise) else ""

	@computed(models.DecimalField("标价",max_digits = 10,decimal_places = 2), depends=[['merchandise', ['price']]])
	def price(self):
		return self.merchandise.price if self.merchandise else 0

	#销售信息
	#deduct = models.FloatField("优惠",default=0)
	actrual_price = models.DecimalField("售价",default = 0,max_digits = 10,decimal_places = 2)

	order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		related_name="sales_record",
		verbose_name="订单"
	)
	package = models.ForeignKey(
		Package,
		null = True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name = "sales_record",
		verbose_name = "包裹"
	)

	def __str__(self):
		return "宝贝"
	class Meta:
		verbose_name = "销售记录"
		verbose_name_plural = verbose_name

class Refund(models.Model):

	date = models.DateTimeField("退货日期",default=timezone.now)
	
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


class RefundRecord(models.Model):
	refund = models.ForeignKey(
		Refund,
		on_delete = models.CASCADE,
		blank = False,
		related_name = "refund_record",
		verbose_name = "退货申请"
	)

	sales_record = models.ForeignKey(
		SalesRecord,
		on_delete = models.CASCADE,
		blank = False,
		related_name = "refund_record",
		verbose_name = "销售记录"
	)
	
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

#支出
class Outlay(models.Model):
	pass

#维修单
class Repair(models.Model):
	pass




class Pay(models.Model):
	is_income = models.BooleanField("收入",default=True)
	PAY_TYPE = (
		("CASH","现金"),
		("BANK","银行转账"),
		("CRED","信用卡付款"),
		("WXZF","微信支付"),
		("WXZZ","微信转账"),
		("WXHB","微信红包"),
		("APZF","支付宝支付"),
		("APZZ","支付宝转账"),
		("BLCE","店内余额"),
	)
	pay_type = models.CharField("付款方式",choices=PAY_TYPE,max_length=4)
	amount = models.DecimalField("付款金额",max_digits = 10,decimal_places = 2)
	pay_time = models.DateTimeField("付款时间",default = timezone.now)

	order = models.ForeignKey(
		Order,
		null=True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name="pay",
		verbose_name="订单"
	)
	refund = models.ForeignKey(
		Refund,
		null=True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name="pay",
		verbose_name="退货"
	)

	img = models.ImageField("截图",blank=True)
	def __str__(self):
		return str(self.order_id)
	class Meta:
		verbose_name = "付款"
		verbose_name_plural = verbose_name	

	