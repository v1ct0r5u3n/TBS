from django.contrib import admin

# Register your models here.
from .models import Depot,Jewel,Accessory,Pearl,Diamond,Certificate,ColoredGem
from django.utils.html import mark_safe

@admin.register(Jewel)
class JewelAdmin(admin.ModelAdmin):
	list_display = ['description','sku','price','jewel_type','style','depot','thumbnail',]
	
	def thumbnail(self,obj):
		if obj.img:
			return mark_safe('<img src="{url}" height=70 />'.format(url = obj.img.url))
	
	thumbnail.short_description = '图像'


admin.site.register(Depot)
#admin.site.register(Jewel)
admin.site.register(Accessory)
admin.site.register(Pearl)
admin.site.register(Diamond)
admin.site.register(Certificate)
admin.site.register(ColoredGem)
