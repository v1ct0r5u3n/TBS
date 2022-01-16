# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record

class Disassemble(Record):
	manufacture = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return '=>'+self.manufacture.lable

	class Meta:
		verbose_name = "拆货单"
		verbose_name_plural = verbose_name

class Assemble(Record):
	manufacture = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return self.manufacture.lable+'=>'

	class Meta:
		verbose_name = "组装单"
		verbose_name_plural = verbose_name
