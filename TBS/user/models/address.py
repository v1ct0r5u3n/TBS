# -*- coding: utf-8 -*-
from django.db import models

class Area(models.Model):
	name = models.CharField("名称",max_length=20)
	parent=models.ForeignKey(
		"self",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name="所属"
	)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "省市区"
		verbose_name_plural = verbose_name


class Address(models.Model):
	default = models.BooleanField("默认地址",default=True)
	lable = models.CharField("标签",max_length=20,blank=True,default="")

	name = models.CharField("收货人",max_length=20)
	phone = models.CharField("电话",max_length=20)
	area = models.ForeignKey(
		Area,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name = "more_detail",
		verbose_name="上级省市区",
	)
	detail = models.CharField("详细地址",max_length=200)
	def __str__(self):
		return self.lable
	class Meta:
		verbose_name = "地址"
		verbose_name_plural = verbose_name
		