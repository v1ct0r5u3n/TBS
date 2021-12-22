# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Area(models.Model):
	name = models.CharField("名称",max_length=20)
	parent=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="所属")
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "省市区"
		verbose_name_plural = verbose_name

class Address(models.Model):
	lable = models.CharField("标签",max_length=20,default="默认地址")
	name = models.CharField("收货人",max_length=20)
	phone = models.IntegerField("电话")
	area = models.ForeignKey(Area,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="省市区")
	detail = models.CharField("详细地址",max_length=200)
	def __str__(self):
		return self.lable
	class Meta:
		verbose_name = "地址"
		verbose_name_plural = verbose_name

class Merchandise(models.Model):
	product_id = models.IntegerField(primary_key=True,unique=True)

	description = models.CharField("描述",max_length = 50)
	net_weight = models.IntegerField("净重")
	amount = models.IntegerField("件数",default=1)

	supplier = models.ForeignKey('Depot',on_delete=models.SET_NULL,null=True)
	
	supply_date = models.DateTimeField("入库时间",default = timezone.now)
	manufacture = models.CharField("产地",max_length=10)
	cost = models.FloatField("成本")
	
	depot = models.ForeignKey('Depot',on_delete=models.SET_NULL,null=True)
	price = models.FloatField("标价")
	margin = models.FloatField("价格浮动")

	deleted = models.BooleanField(default=False)
	def __str__(self):
		return self.description
	class Meta:
		virtual = True

class Gem(Merchandise):
	mount = models.ForeignKey(
		"Mount",
		null = True,
		default = null,
		on_delete=models.SET_NULL,
		related_name = "sub_gem",
		verbose_name = "配石"
		)
	jewel = models.ForeignKey(
		"Jewel",
		null = True,
		default = null,
		on_delete = models.SET_NULL,
		related_name = "main_gem",
		verbose_name = "主石"
		)
	class Meta:
		virtual = True
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
	min_size = models.FloatField()
	max_size = models.FloatField()

	#color
	body_color = models.CharField("体色",max_length=10)
	overtone = models.CharField("伴色",max_length=10)
	IRIDESCENCE = (("","N/A"),("A","强"),("B","明显"),("C","一般"))
	iridescence = models.CharField("晕彩",max_length=1,choices=IRIDESCENCE)

	LUSTER = (("","N/A"),("A","极强"),("B","强"),("C","中"),("D","弱"))
	luster = models.CharField(max_length=1,choices=LUSTER)

	SURFACE = (("","N/A"),("A","无瑕"),("B","微瑕"),("C","小瑕"),("D","瑕疵"),("E","重瑕"))
	surface = models.CharField(max_length=1,choices=SURFACE)

	NACRE = (("","N/A"),("A","特厚"),("B","厚"),("C","中"),("D","薄"),("E","极薄"))
	nacre = models.CharField(max_length=1,choices=NACRE)

	TYPE = (
		("AW","澳白")，
		("TB","大溪地黑珍珠"),
		("SG","南洋金"),
		("AK","AKOYA")，
		("FW","淡水珍珠"),
		("ED","爱迪生珍珠"),
		)

class AbnormityPearl(Pearl):
	SHAPE_TYPE = (
		("CONC","海螺珠"),
		("WTDP","水滴"),
		("MABE","马贝"),
		("BARQ","巴洛克"),
		("KESH","KESHI"),
		)



class Metal(Merchandise):
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
		)
	metal_type = models.CharField(max_length=4,choices = METAL_TYPE)
	

class Mount(Merchandise):
	'''空托'''
	metal = models.ForeignKey(Metal,on_delete=models.SET_NULL)


class PriceCategory(models.Model):
	description = models.CharField(max_length = 50)

class Jewel(models.Model):
	
	major_stone = models.ForeignKey(Stone,on_delete=models.SET_NULL)
	major_stone_description = models.CharField(max_length=50)

	metal = models.ForeignKey(Metal,on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name = "成品"
		verbose_name_plural = verbose_name
	
	

class Depot(models.Model):
	'''
	仓库
	'''
	SUPPLIER = 'SL'
	WAREHOUSE = 'WH'
	RETAIL_STORE = 'ST'
	AGENT = 'AG'
	MAINTENANCE = 'MT'

	DEPOT_TYPE = [
		(SUPPLIER,'供应商'),
		(WAREHOUSE,'仓库'),
		(RETAIL_STORE,'直营店'),
		(AGENT,'代理商'),
		(MAINTENANCE,'维修厂'),
	]

	depot_type = models.CharField(max_length=2,choices=DEPOT_TYPE,blank=False,default=WAREHOUSE)
	address = models.ForeignKey(Address,on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name = "任务"
		verbose_name_plural = verbose_name
	

class Person(models.Model)
	name = models.CharField("姓名",max_length=20)
	mobile = models.IntegerField("手机")
	wechat = models.CharField("微信号",max_length=50)
	address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="地址")
	def __str__(self):
		return self.name
	class Meta:
		virtual = True

class Employee(Person):
	'''
	雇员.
	'''
	class Meta:
		verbose_name = "员工"
		verbose_name_plural = verbose_name
	

class CustomerRank(models.Model):
	name = models.CharField(max_length=20)
	level = models.PositiveSmallIntegerField(default=1)
	class Meta:
		verbose_name = "VIP等级"
		verbose_name_plural = verbose_name


class Customer(Person):
	'''
	顾客.
	'''
	rank = models.ForeignKey(CustomerRank,on_delete = models.SET_NULL,null=True)
	balance = models.FloatField("余额",default=0)
	due = models.FloatField("欠款",default=0)

	Employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,verbose_name="专属客服")

	class Meta:
		verbose_name = "顾客"
		verbose_name_plural = verbose_name


class Order(models.Model):
	order_id = models.CharField("订单号",primary_key=True,max_length=20)
	total_count = models.IntegerField("总件数")

	ship_fee = models.FloatField("运费")
	packaging = models.FloatField("包装费")
	insurance = models.FloatField("保险")
	other_fee = models.FloatField("其它")

	deduct = models.FloatField("扣减金额")
	total_value = models.FloatField("总价")

	ship_date = models.DateTimeField("发货日期",null = True,default = null)
	carrier = models.CharField("承运",blank=True,default="自提",max_length=20)
	track_no = models.CharField("运单号",blank = True,default = "",max_length=20)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	class Meta:
		verbose_name = "订单"
		verbose_name_plural = verbose_name
	

class SalesRecord(models.Model):
	order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		related_name="sales_record",
		verbose_name="订单"
		)
	employee = models.ForeignKey(
		Employee,
		on_delete=models.CASCADE,
		related_name="sales_record",
		verbose_name="销售"
		)
	share = models.FloatField("销售额分成")

	class Meta:
		verbose_name = "销售记录"
		verbose_name_plural = verbose_name

	