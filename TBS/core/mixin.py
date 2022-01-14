# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedMixin(models.Model)
	created = models.DateTimeField("创建时间",auto_now_add = True)
	modified = models.DecimalField("修改时间",auto_now = True)
	class Meta:
		abstract = True

