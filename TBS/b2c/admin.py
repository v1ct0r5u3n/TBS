from django.contrib import admin
from .models import Order,Package,SalesRecord,Refund,RefundRecord,SalesShare,Pay
from user.models import Customer
from django.utils.html import mark_safe
from jewelry.models import Merchandise
import nested_admin
# Register your models here.

#admin.StackedInline
class CustomerInline(nested_admin.NestedTabularInline):
	model = Customer
	extra = 1

class MerchandiseInline(nested_admin.NestedTabularInline):
	model = Merchandise
	extra = 1
	

class SalesRecordInline(nested_admin.NestedTabularInline):
	model = SalesRecord
	extra = 1
	#inlines = [MerchandiseInline]
	readonly_fields = ['thumbnail']

	@admin.display(description='图像')
	def thumbnail(self,obj):
		return mark_safe('<img src="{url}" height=100 />'.format(url = obj.merchandise.img.url)
	)

class SalesShareInline(nested_admin.NestedTabularInline):
    model = SalesShare
    extra = 1

class PayInline(nested_admin.NestedTabularInline):
	model = Pay
	exclude = ("refund",)
	extra = 0

@admin.register(Order)
class OrderAdmin(nested_admin.NestedModelAdmin):
#	date_hierarchy = 'order_date'

	list_display = ['order_id','customer','order_date','merchandise_count','total_value']
	readonly_fields = ['order_date','last_change','order_id','merchandise_count']
	#autocomplete_fields = ['customer']
	raw_id_fields = ["customer"]


	fieldsets = [
		(None, {'fields': (('order_date','last_change'),'order_id','customer',)}),
	    ('总计',{'fields': (('deduct','total_value',),)}),
	    (None,{'fields': ('comments',)}),
	]

	inlines = [SalesRecordInline,SalesShareInline,PayInline]

	@admin.display(description='件数')
	def merchandise_count(self,obj):
		return obj.sales_record.count()
	

#admin.site.register(Order,OrderAdmin)
#admin.site.register(Package)
#admin.site.register(SalesRecord)
admin.site.register(Refund)
#admin.site.register(RefundRecord)
#admin.site.register(SalesShare)
#admin.site.register(Pay)
'''
def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(name__in=['God', 'Demi God'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
'''