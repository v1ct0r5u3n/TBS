# -*- coding: utf-8 -*-
from django.db import models
from .merchandise import Merchandise
from core.mixins import ThumbnailMixin

class Certificate(ThumbnailMixin,models.Model):
	CERTIFICATE_BY=(
		("","N/A"),
		("NJC","中国国家首饰质量检验检测中心(NJC)"),
		("PSL","日本真珠科学研究所(PSL)"),
		("PEPCA","日本真珠输出加工协同组合(PEPCA)"),
		("PIC","日本真珠综合研究所(PIC)"),
		("GIA","美国宝石学院(GIA)"),
		("IGI","国际宝石学院(IGI)"),
		("AGS","美国宝石学会(AGS)"),
		("EGL","欧洲宝石学实验室(EGL)"),
	)
	issuer = models.CharField("颁发机构",max_length=5,default="",choices=CERTIFICATE_BY)
	code = models.CharField("证书编号",max_length=50,default="",blank=True)
	merchandise = models.ForeignKey(
		Merchandise,
		on_delete=models.CASCADE,
		blank=False,
		related_name = "certificate",
		verbose_name = "证书",
	)
	def __str__(self):
		return self.issuer+":"+code
	class Meta:
		verbose_name = "证书"
		verbose_name_plural = verbose_name

