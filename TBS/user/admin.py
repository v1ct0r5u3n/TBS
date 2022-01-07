from django.contrib import admin

# Register your models here.
from .models import Address,Employee,Customer,Person

admin.site.register(Address)
admin.site.register(Employee)
#admin.site.register(Customer)
#admin.site.register(Person)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	search_fields = ['name','mobile','wechat']
