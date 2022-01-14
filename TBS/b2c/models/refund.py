# -*- coding: utf-8 -*-


class Refund(Record,TimeStampedMixin):

	date = models.DateTimeField("退货日期",default=timezone.now)
	
	customer = models.ForeignKey(
		Customer,
		null = True,
		blank = True,
		on_delete = models.SET_NULL,
		related_name = "refund_record",
		verbose_name = "顾客"
	)

	actrual_price = models.DecimalField("退款金额",default = 0,max_digits = 10,decimal_places = 2)

	def __str__(self):
		return str(self.order_id)
	class Meta:
		verbose_name = "退款"
		verbose_name_plural = verbose_name


class MechandiseRefund(MerchandiseRecord):
	refund = models.ForeignKey(
		Refund,
		on_delete = models.CASCADE,
		blank = False,
		related_name = "refund_record",
		verbose_name = "退货申请"
	)

	sales_record = models.ForeignKey(
		SalesRecord,
		on_delete = models.CASCADE,
		blank = False,
		related_name = "refund_record",
		verbose_name = "销售记录"
	)
	
	package = models.ForeignKey(
		Package,
		null = True,
		blank = True,
		on_delete=models.SET_NULL,
		related_name = "refund_record",
		verbose_name = "包裹"
	)

	def __str__(self):
		return "退货记录"
	class Meta:
		verbose_name = "退货记录"
		verbose_name_plural = verbose_name
