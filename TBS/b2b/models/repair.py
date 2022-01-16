# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record
'''
class Repair(Record):
	manufacture = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return '=>'+self.manufacture.lable

	class Meta:
		verbose_name = "维修单"
		verbose_name_plural = verbose_name

class RepairReturn(Record):
	manufacture = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return self.manufacture.lable+'=>'

	class Meta:
		verbose_name = "维修返单"
		verbose_name_plural = verbose_name
'''