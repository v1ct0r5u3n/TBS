# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone
from user.models import Person,Customer
from .depot import Depot
from core.models import Address
from core.mixins import TimeStampedMixin,PartComposMixin
#from .relationship import Record
# Create your models here.

class PriceCategory(models.Model):
	description = models.CharField(max_length = 50)
	#标价基础倍率
	#提成

class Sku(models.Model):
	sku = models.CharField("款号",max_length = 20)
	description = models.CharField("描述",max_length = 50,blank=True)
	def __str__(self):
		return self.sku
	class Meta:
		verbose_name = "款式"
		verbose_name_plural = verbose_name


class Merchandise(TimeStampedMixin,PartComposMixin,models.Model):
	#filterout deleted objects
	#objects = MerchandiseManager()

	img = models.ImageField("图像",null=True, blank=True, upload_to="thumbnail/")

	description = models.CharField("描述",max_length = 50)
	net_weight = models.FloatField("净重(g)",blank=True)

	def carat(self):
		return self.net_weight/0.2
	carat.short_description = '克拉(Ct)'
	carat.admin_order_field = 'net_weight'

	sku = models.ForeignKey(
		Sku,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='merchandise',
		verbose_name='款式',
	)
	
	depot = models.ForeignKey(
		Depot,
		on_delete=models.SET_NULL,
		null=True,
		related_name = "instock",
		verbose_name = "场所"
	)
	position = models.CharField("库柜",max_length=20,blank=True)

	price = models.DecimalField("标价",default = 0,max_digits = 10,decimal_places = 2)
	margin = models.DecimalField("价格浮动",default = 0,max_digits = 10,decimal_places = 2)

	records = models.ManyToManyField(
		'Record',
		through='MerchandiseRecord',
		related_name='merchandises'
	)

	def __str__(self):
		return self.description


# chain or ring have size

class Jewel(Merchandise):
	JEWEL_TYPE = (
		("","N/A"),
		("R","戒指"),
		("项链",(
			("P","项坠"),
			("N","珠链"),
		)),
		("耳饰",(
			("D","耳钉"),
			("G","耳钩"),
			("X","耳线"),
			("J","耳夹"),
		)),
		("W","手链"),
		("B","胸针"),
		("H","头饰"),
	)
	
	jewel_type = models.CharField('类别',max_length=5,choices=JEWEL_TYPE,default="")
	size = models.DecimalField('长度/手寸',default = 0,max_digits = 5,decimal_places = 2)

	def __str__(self):
		return "成品"+self.description
	class Meta:
		verbose_name = "成品"
		verbose_name_plural = verbose_name
	

class Accessory(Merchandise):

	jewel_type = models.CharField('类别',max_length=5,choices=Jewel.JEWEL_TYPE,default="")
	size = models.DecimalField('长度/手寸',default = 0,max_digits = 5,decimal_places = 2)

	METAL_TYPE = (
		("PT","铂金"),
		("24KG","24K金"),
		("18KY","18K黄"),
		("18KW","18K白"),
		("18KR","18K红"),
		("14KY","14K黄"),
		("14KW","14K白"),
		("14KR","14K红"),
		("10KY","14K黄"),
		("10KW","14K白"),
		("10KR","14K红"),
		("SILV","纯银"),
		("S925","S925"),
		("GONB","铜镀金"),
		("ALLO","合金"),
		("","N/A")
	)
	metal_type = models.CharField('金属',max_length=4,choices = METAL_TYPE,default="")

	def __str__(self):
		return self.description
	class Meta:
		verbose_name = "配件"
		verbose_name_plural = verbose_name
	


class Gem(Merchandise):
	pass
'''
size, 直径
shape, 形状
color, 颜色
luster, 光泽
surface, 表皮
nacre，珠层
'''
#大小 光泽 瑕疵 颜色
#圆珠 圆度（正圆，近圆，扁圆）
#水滴
#mabe
#巴洛克 keshi（无核）
class Pearl(Gem):
	PEARL_TYPE = (
		("","N/A"),
		("海水珍珠",(
				("AWHT","南洋白珍珠"),
				("SSGD","南洋金珍珠"),
				("TBLK","大溪地黑珍珠"),
				("AKOY","AKOYA"),
				("MABE","马贝珠"),
				("KESH","KESHI"),
				("CONC","海螺珠"),
			)
		),
		("淡水珍珠",(
				("FRWT","淡水珍珠"),
				("BARQ","巴洛克珍珠"),
				("EDSN","爱迪生珍珠"),
			)
		)
	)

	pearl_type = models.CharField(max_length=4,choices=PEARL_TYPE,default="")

	min_size = models.DecimalField("最小直径(mm)",default = 0,max_digits = 5,decimal_places = 2)
	max_size = models.DecimalField("最大直径(mm)",default = 0,max_digits = 5,decimal_places = 2)

	#color
	body_color = models.CharField("体色",max_length=10)
	overtone = models.CharField("伴色",max_length=10)
	IRIDESCENCE = (("","N/A"),("A","强"),("B","明显"),("C","一般"))
	iridescence = models.CharField("晕彩",max_length=1,choices=IRIDESCENCE,default="")

	LUSTER = (("","N/A"),("A","极强"),("B","强"),("C","中"),("D","弱"))
	luster = models.CharField("光泽",max_length=1,choices=LUSTER)

	SURFACE = (("","N/A"),("A","无瑕"),("B","微瑕"),("C","小瑕"),("D","瑕疵"),("E","重瑕"))
	surface = models.CharField("表皮",max_length=1,choices=SURFACE)

	NACRE = (("","N/A"),("A","特厚"),("B","厚"),("C","中"),("D","薄"),("E","极薄"))
	nacre = models.CharField("珠层",max_length=1,choices=NACRE)

	def __str__(self):
		return "珍珠"
	class Meta:
		verbose_name = "珍珠"
		verbose_name_plural = verbose_name

class Diamond(Gem):
	COLOR = (
		("","N/A"),
		("D","D"),
		("E","E"),
		("F","F"),
		("G","G"),
		("H","H"),
		("I","I"),
		("J","J"),
		("K","K"),
	)
	color = models.CharField("颜色",max_length=1,choices=COLOR,default="")

	CLARITY = (
		("","N/A"),
		("FL","FL"),
		("IF","IF"),
		("VVS1","VVS1"),
		("VVS2","VVS2"),
		("VS1","VS1"),
		("VS2","VS2"),
		("SI1","SI1"),
		("SI2","SI2"),
	)
	clarity = models.CharField("净度",max_length=4,choices=CLARITY,default="")

	CUT = (
		("","N/A"),
		("EX","EX"),
		("VG","VG"),
		("G","G"),
	)
	cut = models.CharField("切工",max_length=2,choices=CUT,default="")
	def __str__(self):
		return "钻石"+"{:.2f}".format(self.net_weight/0.2)+"ct"
	class Meta:
		verbose_name = "钻石"
		verbose_name_plural = verbose_name

class ColoredGem(Gem):
	def __str__(self):
		return "彩宝"
	class Meta:
		verbose_name = "彩宝"
		verbose_name_plural = verbose_name
		proxy = True



