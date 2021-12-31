# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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

class Person(models.Model):
	name = models.CharField("姓名",max_length=20)
	mobile = models.IntegerField("手机")
	wechat = models.CharField("微信号",max_length=50)
	alipay = models.CharField("支付宝",max_length=50)
	def __str__(self):
		return self.name
	#class Meta:
	#	abstract = True

class Address(models.Model):
	default = models.BooleanField("默认地址",default=True)
	lable = models.CharField("标签",max_length=20,blank=True,default="")
	person = models.ForeignKey(
		Person,
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name="address",
		verbose_name="联系人",
	)
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
		
class Person(models.Model):
	name = models.CharField("姓名",max_length=20)
	mobile = models.CharField("手机",max_length=20)
	wechat = models.CharField("微信号",max_length=50)
	address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="地址")
	def __str__(self):
		return self.name
	class Meta:
		abstract = True

class Employee(Person):
	'''员工.'''
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	class Meta:
		verbose_name = "员工"
		verbose_name_plural = verbose_name
	

class CustomerRank(models.Model):
	name = models.CharField(max_length=20)
	level = models.PositiveSmallIntegerField(default=1)
	class Meta:
		verbose_name = "VIP等级"
		verbose_name_plural = verbose_name


class Customer(Person):
	'''顾客.'''
	rank = models.ForeignKey(CustomerRank,on_delete = models.SET_NULL,null=True,verbose_name="等级")
	balance = models.FloatField("余额",default=0)
	due = models.FloatField("欠款",default=0)

	Employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,verbose_name="专属客服")

	class Meta:
		verbose_name = "顾客"
		verbose_name_plural = verbose_name
