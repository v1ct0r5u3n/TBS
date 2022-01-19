# -*- coding: utf-8 -*-
from django.db import models
import os
from datetime import datetime
from django.utils import timezone
from django.utils.deconstruct import deconstructible

class OperatorMixin(models.Model):
	operator = models.ForeignKey('user.Employee',on_delete=models.SET_NULL,null=True)
	class Meta:
		abstract = True

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

def _rename_img(instance,filename):
	ext = filename.split('.')[-1]

	#workaround for simpleui
	if ext=='jpeg':
		ext = 'jpg'

	# get filename
	if instance.pk:
		filename = '{}.{}'.format(instance.pk, ext)
	else:
		# set filename as random string
		dt = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
		filename = '{}.{}'.format(dt, ext)
	# return the whole path to the file
	return os.path.join(instance.__class__.__name__, filename)

class ThumbnailMixin(models.Model):
	img = models.ImageField("图片",null=True, blank=True, upload_to = _rename_img)
	class Meta:
		abstract = True


