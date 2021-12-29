from django.contrib import admin
from .models import Order,Package,SalesRecord,Refund,RefundRecord,SalesShare,Pay
# Register your models here.
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(SalesRecord)
admin.site.register(Refund)
admin.site.register(RefundRecord)
admin.site.register(SalesShare)
admin.site.register(Pay)