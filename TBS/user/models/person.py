# -*- coding: utf-8 -*-
from datetime import date
from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from core.mixins import TimeStampedMixin

# Create your models here.


class Person(TimeStampedMixin,models.Model):
	name = models.CharField("姓名",max_length=20,blank = True)
	alias = models.CharField("称呼/别名",max_length=20,blank = True)
	mobile = models.CharField("手机",max_length=20,unique = True)
	wechat = models.CharField("微信号",max_length=50,blank = True)
	alipay = models.CharField("支付宝",max_length=50,blank = True)
	
	def __str__(self):
		return self.name or self.alias or self.mobile


class EmployeeManager(BaseUserManager):
	def create_user(self,mobile,name,password=None):
		if not mobile:
			raise ValueError('员工必须有手机号')

		user = self.model(
			mobile = mobile,
			name = name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self,mobile,name,password=None):
		user = self.create_user(
			mobile,name,
			password=password
		)
		user.is_admin = True
		user.save(using=self._db)
		return user

class Employee(AbstractBaseUser,Person):
	'''员工.'''
	objects = EmployeeManager()

	hire_date = models.DateField("入职时间",blank = False,default=date.today)
	id_card_no = models.CharField("身份证号",max_length = 18,blank = True)
	id_address = models.CharField("身份证地址",max_length = 100,blank = True)

	is_active = models.BooleanField("在职",default=True)
	is_admin = models.BooleanField("管理员",default=False)

	USERNAME_FIELD = 'mobile'
	REQUIRED_FIELDS = ['name']

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		if app_label=='user':
			return self.is_admin
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_active

	def __str__(self):
		return self.name

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

	personal_manager = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,verbose_name="专属客服")

	class Meta:
		verbose_name = "顾客"
		verbose_name_plural = verbose_name

class Supplier(Person):
	class Meta:
		proxy = True

class Agent(Person):
	class Meta:
		proxy = True

