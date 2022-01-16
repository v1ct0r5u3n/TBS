# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone
from .order import Order
from .refund import Refund

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
	value = models.DecimalField("付款金额",max_digits = 10,decimal_places = 2)
	pay_time = models.DateTimeField("付款时间",default = timezone.now)

	order = models.ForeignKey(
		Order,
		null=True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name="pays",
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

	