# -*- coding: utf-8 -*-
from django.db import models

class PriceCategory(models.Model):
	description = models.CharField(max_length = 50)
	#标价基础倍率
	magnify = models.DecimalField('基础倍率',max_digits = 5,decimal_places = 2)
	def __str__(self):
		return self.description
	class Meta:
		verbose_name = "定价类型"
		verbose_name_plural = verbose_name

#提成
class Commision(models.Model):
	lower_bound = models.DecimalField("最低折扣(%)",max_digits=3,decimal_places=1)
	upper_bound = models.DecimalField("最高折扣(%)",max_digits=3,decimal_places=1)
	thousandth = models.DecimalField("提成(‰)",max_digits=4,decimal_places=1)

	price_category = models.ForeignKey(PriceCategory,on_delete=models.CASCADE)