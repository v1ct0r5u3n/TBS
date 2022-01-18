
from .models import Order,Refund
from user.models import Customer
from django.utils.html import mark_safe
from jewelry.models import Merchandise
from django.contrib import admin
#import nested_admin as admin
from nested_admin import NestedTabularInline as TabularInline
from nested_admin import NestedModelAdmin as ModelAdmin
# Register your models here.

#admin.StackedInline

class CustomerInline(TabularInline):
	model = Customer
	extra = 1

class MerchandiseInline(TabularInline):
	model = Merchandise
	extra = 1

	readonly_fields = ['thumbnail']

	@admin.display(description='图像')
	def thumbnail(self,obj):
		return mark_safe('<img src="{url}" height=100 />'.format(url = obj.merchandise.img.url)
	)


@admin.register(Order)
class OrderAdmin(ModelAdmin):
#	date_hierarchy = 'order_date'

	list_display = ['id','customer','created','merchandise_count','total_value']
	date_hierarchy = 'created'

	readonly_fields = ['created','modified','id','merchandise_count']
	#autocomplete_fields = ['customer']
	autocomplete_fields = ["customer"]


	fieldsets = [
		(None, {'fields': (('order_date','modified'),'id','customer',)}),
	    ('总计',{'fields': (('deduct','total_value',),)}),
	    (None,{'fields': ('comments',)}),
	]

#	inlines = [SalesRecordInline,SalesShareInline,PayInline]

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