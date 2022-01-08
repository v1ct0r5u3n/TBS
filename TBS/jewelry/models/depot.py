# -*- coding: utf-8 -*-
from django.db import models
from user.models import Person,Address

class Depot(models.Model):
	SUPPLIER = 'SL'
	WAREHOUSE = 'WH'
	RETAIL_STORE = 'ST'
	AGENT = 'AG'
	MAINTENANCE = 'MT'

	DEPOT_TYPE = [
		(SUPPLIER,'供应商'),
		(WAREHOUSE,'仓库'),
		(RETAIL_STORE,'直营店'),
		(AGENT,'代理商'),
		(MAINTENANCE,'维修厂'),
	]

	lable = models.CharField("名称",max_length=20)

	depot_type = models.CharField(max_length=2,choices=DEPOT_TYPE,blank=False,default=WAREHOUSE)
	contact = models.ForeignKey(
		Person,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name = "+",
		verbose_name = "联系人"
	)
	address = models.ForeignKey(
		Address,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name = "+",
		verbose_name = "地址"
	)
	
	def __str__(self):
		return self.lable
	class Meta:
		verbose_name = "场所"
		verbose_name_plural = verbose_name
