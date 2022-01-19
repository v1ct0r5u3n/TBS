# -*- coding: utf-8 -*-
from django.db import models
from core.mixins import TimeStampedMixin,ThumbnailMixin,OperatorMixin

class Package(	TimeStampedMixin,
				ThumbnailMixin,
				OperatorMixin,
				models.Model):
	ship_date = models.DateTimeField("发货日期",null = True,blank = True)
	sign_date = models.DateTimeField("签收日期",null=True,blank = True)

	carrier = models.CharField("承运",blank=True,default="自提",max_length=20)
	track_no = models.CharField("运单号",blank = True,default = "",max_length=20)
	gross_weight = models.FloatField("毛重",default=0)

	ship_fee = models.DecimalField("运费",default=0,max_digits = 10,decimal_places = 2)
	packaging = models.DecimalField("包装费",default=0,max_digits = 10,decimal_places = 2)
	insurance = models.DecimalField("保险",default=0,max_digits = 10,decimal_places = 2)
	other_fee = models.DecimalField("其它",default=0,max_digits = 10,decimal_places = 2)

	is_payed_on_arrival = models.BooleanField("到付",default=False)
	is_signed = models.BooleanField("签收",default=False)

	def __str__(self):
		return "包裹"
	class Meta:
		verbose_name = "包裹"
		verbose_name_plural = verbose_name