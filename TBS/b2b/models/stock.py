# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record

class Stock(Record):
	supplier = models.ForeignKey(
		Depot,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name="供货商",
		limit_choices_to={'depot_type':Depot.SUPPLIER},
	)
	
	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = "进货单"
		verbose_name_plural = verbose_name


