# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record


#借货单
class Lend(Record):
	agent = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return '=>'+self.agent.lable

	class Meta:
		verbose_name = "借货单"
		verbose_name_plural = verbose_name

class LendReturn(Record):
	agent = models.ForeignKey(Depot,on_delete=models.CASCADE)

	def __str__(self):
		return self.agent.lable+'=>'

	class Meta:
		verbose_name = "还货单"
		verbose_name_plural = verbose_name