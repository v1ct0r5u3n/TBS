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

class Depot(models.Model):
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
		verbose_name = "场所"
		verbose_name_plural = verbose_name

class Merchandise(models.Model):
	CERTIFICATE_BY=(
		("","N/A"),
		("NJC","中国国家首饰质量检验检测中心(NJC)"),
		("PSL","日本真珠科学研究所(PSL)"),
		("PIC","日本真珠综合研究所(PIC)"),
		("GIA","美国宝石学院(GIA)"),
		("IGI","国际宝石学院(IGI)"),
		("AGS","美国宝石学会(AGS)"),
		("EGL","欧洲宝石学实验室(EGL)"),
	)
	certificate_by=models.CharField("证书机构",max_length=5,default="")
	certificate = models.CharField("证书编号",max_length=50,default="")
	img = models.ImageFiled("图像")

	description = models.CharField("描述",max_length = 50)
	net_weight = models.FloatField("净重")

	sku = models.CharField(
		"款号",
		max_length = 20,
		help_text = "配对的两颗宝石拥有相同sku"+
					"整包裸石拥有相同的sku"+
					"套装成品拥有相同的sku"+
					"同款多件拥有相同的sku"
	)
	sku_count = models.IntegerField("同款",default=1)
	sku_description = models.CharField("款式",max_length=20)
	
	supplier = models.ForeignKey('Depot',on_delete=models.SET_NULL,null=True,verbose_name="供货商")
	supply_date = models.DateTimeField("入库时间",default = timezone.now)
	manufacture = models.CharField("产地",max_length=10)
	cost = models.FloatField("成本")
	
	depot = models.ForeignKey(Depot,on_delete=models.SET_NULL,null=True)
	price = models.FloatField("标价")
	margin = models.FloatField("价格浮动")

	deleted = models.BooleanField(default=False)
	def __str__(self):
		return self.description
	class Meta:
		virtual = True

class Accessory(Merchandise):
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
	metal_type = models.CharField(max_length=4,choices = METAL_TYPE,default="")
	def __str__(self):
		return "配件"+self.description
	class Meta:
		verbose_name = "配件"
		verbose_name_plural = verbose_name
	


class Gem(Merchandise):

	accessory = models.ForeignKey(
		"Accessory",
		null = True,
		default = NULL,
		on_delete=models.SET_NULL,
		related_name = "sub_gem",
		verbose_name = "所属空托或配件",
		help_text = "如果是配石"
	)

	jewel = models.ForeignKey(
		"Jewel",
		null = True,
		default = NULL,
		on_delete = models.SET_NULL,
		related_name = "main_gem",
		verbose_name = "所属成品",
		help_text = "如果是主石"
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
	PEARL_ALIAS = (
		("tn","天女"),
	)
	pearl_alias = models.CharField(max_length=4,choices=,default="")
	min_size = models.FloatField()
	max_size = models.FloatField()

	#color
	body_color = models.CharField("体色",max_length=10)
	overtone = models.CharField("伴色",max_length=10)
	IRIDESCENCE = (("","N/A"),("A","强"),("B","明显"),("C","一般"))
	iridescence = models.CharField("晕彩",max_length=1,choices=IRIDESCENCE,default="")

	LUSTER = (("","N/A"),("A","极强"),("B","强"),("C","中"),("D","弱"))
	luster = models.CharField(max_length=1,choices=LUSTER)

	SURFACE = (("","N/A"),("A","无瑕"),("B","微瑕"),("C","小瑕"),("D","瑕疵"),("E","重瑕"))
	surface = models.CharField(max_length=1,choices=SURFACE)

	NACRE = (("","N/A"),("A","特厚"),("B","厚"),("C","中"),("D","薄"),("E","极薄"))
	nacre = models.CharField(max_length=1,choices=NACRE)

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
	color = models.CharField(max_length=1,choices=COLOR,default="")

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
	clarity = models.CharField(max_length=4,choices=CLARITY,default="")

	CUT = (
		("","N/A"),
		("EX","EX"),
		("VG","VG"),
		("G","G"),
	)
	cut = models.CharField(max_length=2,choices=CUT,default="")
	def __str__(self):
		return "钻石"+"{.2f}".format(self.net_weight/0.2)+"ct"
	class Meta:
		verbose_name = "钻石"
		verbose_name_plural = verbose_name


class PriceCategory(models.Model):
	description = models.CharField(max_length = 50)

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
	
	jewel_type = models.CharField(max_length=5,choices=JEWEL_TYPE,default="")
	style = models.CharField(
		"风格",
		max_length = 100,
		blank = True,
		default = "",
		help_text = "工艺或风格系列，例如花丝、满天星"
	)

	def __str__(self):
		return "成品"+self.description
	class Meta:
		verbose_name = "成品"
		verbose_name_plural = verbose_name
	
class Person(models.Model):
	name = models.CharField("姓名",max_length=20)
	mobile = models.IntegerField("手机")
	wechat = models.CharField("微信号",max_length=50)
	address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="地址")
	def __str__(self):
		return self.name
	class Meta:
		virtual = True

class Employee(Person):
	'''员工.'''
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
	'''顾客.'''
	rank = models.ForeignKey(CustomerRank,on_delete = models.SET_NULL,null=True)
	balance = models.FloatField("余额",default=0)
	due = models.FloatField("欠款",default=0)

	Employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,verbose_name="专属客服")

	class Meta:
		verbose_name = "顾客"
		verbose_name_plural = verbose_name

class Order(models.Model):
	'''订单.'''
	order_id = models.BigAutoField(primary_key=True)
	order_date = models.DateTimeField("订单日期",default=timezone.now)
	total_count = models.IntegerField("总件数")

	ship_fee = models.FloatField("运费")
	packaging = models.FloatField("包装费")
	insurance = models.FloatField("保险")
	other_fee = models.FloatField("其它")

	deduct = models.FloatField("优惠金额")
	total_value = models.FloatField("总价")

	ship_date = models.DateTimeField("发货日期",null = True,default = null)
	carrier = models.CharField("承运",blank=True,default="自提",max_length=20)
	track_no = models.CharField("运单号",blank = True,default = "",max_length=20)

	comments = models.TextField("备注",blank = True,default = "",max_length=100)

	ORDER_STATUS = (("A","新订单"),("B","已付款"),("C","已发货"),("D","已收货"),("E","已关闭"))
	order_status = models.CharField(max_length=1,choices=ORDER_STATUS)

	def __str__(self):
		return str(self.order_id)
	class Meta:
		verbose_name = "订单"
		verbose_name_plural = verbose_name

class Pay(models.Model):
	PAY_TYPE = (
		("CASH","现金"),
		("BANK","银行转账"),
		("CRED","信用卡付款"),
		("WXZF","微信支付"),
		("WXZZ","微信转账"),
		("WXHB","微信红包"),
		("APZF","支付宝支付"),
		("APZZ","支付宝转账"),
		("BLCE","店内余额"),
	)
	
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,related_name="pay",verbose_name="订单")
	amount = models.FloatField("付款金额",default=order.total_value)
	pay_time = models.DateTimeField("付款时间",default = timezone.now)
	img = models.ImageFiled("截图",blank=True)
	

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

	def __str__(self):
		return str(self.order.order_id)+":"+str(self.share*100)+r"%"

	class Meta:
		verbose_name = "销售记录"
		verbose_name_plural = verbose_name

	