# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Person(models.Model):
	name = models.CharField("姓名",max_length=20)
	mobile = models.IntegerField("手机")
	wechat = models.CharField("微信号",max_length=50)
	alipay = models.CharField("支付宝",max_length=50)
	def __str__(self):
		return self.name

class Employee(AbstractUser,Person):
	'''员工.'''
	USERNAME_FIELD = 'mobile'
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
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
	rank = models.ForeignKey(CustomerRank,on_delete = models.SET_NULL,null=True,blank = True,verbose_name="等级")
	balance = models.FloatField("余额",default=0)
	due = models.FloatField("欠款",default=0)

	Employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,verbose_name="专属客服")

	class Meta:
		verbose_name = "顾客"
		verbose_name_plural = verbose_name

class Supplier(Person):
	class Meta:
		proxy = True

class Agent(Person):
	class Meta:
		proxy = True

