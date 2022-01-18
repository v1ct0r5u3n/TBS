# -*- coding: utf-8 -*-
from django.db import models
import os
from datetime import date
from uuid import uuid4
from django.utils import timezone
from django.utils.deconstruct import deconstructible


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
		filename = '{}.{}'.format(uuid4().hex, ext)
	# return the whole path to the file
	return os.path.join(instance.__class__.__name__, filename)

class ThumbnailWithPkAsFilenameMixin(models.Model):
	img = models.ImageField("缩略图",null=True, blank=True, upload_to = _rename_img)
	class Meta:
		abstract = True


