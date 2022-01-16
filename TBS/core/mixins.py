# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone

class TimeStampedMixin(models.Model):
	created = models.DateTimeField("创建时间",auto_now_add = True)
	modified = models.DateTimeField("修改时间",auto_now = True)
	class Meta:
		abstract = True

class PartComposMixin(models.Model):
	belongs_to = models.ForeignKey(
		'self',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name='%(app_label)s_%(class)s'
	)
	class Meta:
		abstract = True