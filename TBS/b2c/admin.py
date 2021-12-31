from django.contrib import admin
from .models import Order,Package,SalesRecord,Refund,RefundRecord,SalesShare,Pay
# Register your models here.

#admin.StackedInline
class SalesRecordInline(admin.TabularInline):
    model = SalesRecord
    extra = 0

class SalesShareInline(admin.TabularInline):
    model = SalesShare
    extra = 1
class PayInline(admin.TabularInline):
	model = Pay
	exclude = ("refund",)
	extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': (('customer','order_date',),)}),
        ('总计',{'fields': (('total_count','deduct','total_value',),)}),
 #       (None,{'fields': ('comments',)}),
    ]

    inlines = [SalesRecordInline,SalesShareInline,PayInline]


#admin.site.register(Order,OrderAdmin)
#admin.site.register(Package)
#admin.site.register(SalesRecord)
admin.site.register(Refund)
#admin.site.register(RefundRecord)
#admin.site.register(SalesShare)
#admin.site.register(Pay)