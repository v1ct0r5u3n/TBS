# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record


#借货单
class B2BRecord(Record):
	depot = models.ForeignKey(Depot,on_delete=models.CASCADE)
	class Meta:
		verbose_name = "操作单"
		verbose_name_plural = verbose_name

class B2BConfirm(B2BRecord):
	record = models.OneToOneField(B2BRecord,on_delete=models.CASCADE,related_name='confirm')
	class Meta:
		verbose_name = "操作确认单"
		verbose_name_plural = verbose_name
