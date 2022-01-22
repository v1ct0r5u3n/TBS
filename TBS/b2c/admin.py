
from .models import Order,Refund,SalesShare
from jewelry.models import Record
from user.models import Customer
from core.models import Pay

from django.utils.html import mark_safe
from jewelry.models import Merchandise
from django.contrib import admin
#import nested_admin as admin
#from nested_admin import NestedTabularInline as TabularInline
#from nested_admin import NestedModelAdmin as ModelAdmin
# Register your models here.

#admin.site.register(Order)
admin.site.register(SalesShare)
#admin.StackedInline

class CustomerInline(admin.TabularInline):
	model = Customer
	extra = 1

class MerchandiseInline(admin.StackedInline):
	model = Merchandise.records.through
	extra = 1

	readonly_fields = ['thumbnail']
	autocomplete_fields = ["merchandise",'record']

	@admin.display(description='图像')
	def thumbnail(self,obj):
		return mark_safe('<img src="{url}" height=100 />'.format(url = obj.merchandise.img.url)
	)

class SalesShareInline(admin.TabularInline):
	model = SalesShare
	extra = 1

class PayInline(admin.TabularInline):
	model = Record.pays.through
	extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'

	readonly_fields = ['created','modified','id','merchandise_count']
	#autocomplete_fields = ['customer']
	autocomplete_fields = ["customer"]

	'''
	fieldsets = [
		(None, {'fields': (('order_date','modified'),'id','customer',)}),
	    ('总计',{'fields': (('deduct','total_value',),)}),
	    (None,{'fields': ('comments',)}),
	]
	'''
	inlines = [MerchandiseInline,SalesShareInline,PayInline]

	@admin.display(description='件数')
	def merchandise_count(self,obj):
		return obj.merchandises.count()


#admin.site.register(Order,OrderAdmin)
#admin.site.register(Package)
#admin.site.register(SalesRecord)

admin.site.register(Refund)
#admin.site.register(RefundRecord)
#admin.site.register(SalesShare)

'''
def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(name__in=['God', 'Demi God'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
'''