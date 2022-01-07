from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Address,Employee,Customer,Person

#admin.site.register(Address)
#admin.site.register(Employee)
#admin.site.register(Customer)
#admin.site.register(Person)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	search_fields = ['name','mobile','wechat']

#@admin.register(Employee)
#class EmployeeAdmin(admin.ModelAdmin):
#	pass
admin.site.register(Employee,UserAdmin)
