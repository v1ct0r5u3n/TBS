from django.contrib import admin

# Register your models here.
from .models import Depot,Sku,Jewel,Accessory,Pearl,Diamond,Certificate,ColoredGem
from django.utils.html import mark_safe

admin.site.register(Sku)

class MerchandiseAdmin(admin.ModelAdmin):
	list_filter = []
	def thumbnail(self,obj):
		if obj.img:
			return mark_safe('<img src="{url}" height=70 />'.format(url = obj.img.url))

	thumbnail.short_description = '图像'

	#def get_deleted_objects(objs, request):
	#	return None
	
	'''

@admin.register(Jewel)
class JewelAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','jewel_type','style','depot','is_tagged','is_sold','thumbnail',]



@admin.register(Accessory)
class AccessoryAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','metal_type','style','depot','is_tagged','is_sold','thumbnail',]
	

@admin.register(Pearl)
class PearlAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','metal_type','style','depot','is_tagged','is_sold','thumbnail',]

@admin.register(Diamond)
class DiamondAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','metal_type','style','depot','is_tagged','is_sold','thumbnail',]

@admin.register(Certificate)
class CertificateAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','metal_type','style','depot','is_tagged','is_sold','thumbnail',]

@admin.register(ColoredGem)
class ColoredGemAdmin(MerchandiseAdmin):
	list_display = ['description','sku','price','metal_type','style','depot','is_tagged','is_sold','thumbnail',]
'''
admin.site.register(Depot,admin.ModelAdmin)
admin.site.register(Certificate,admin.ModelAdmin)

admin.site.register(Jewel,MerchandiseAdmin,list_display=[
			'description',
			'sku',
			'price',
			'jewel_type',
			'depot',
			'thumbnail',
		]
	)

admin.site.register(Accessory,MerchandiseAdmin,list_display=[
			'description',
			'sku',
			'price',
			'metal_type',
			'depot',
			'thumbnail',
		]
	)
admin.site.register(Pearl,MerchandiseAdmin,list_display=[
			'description',
			'sku',
			'price',
			'min_size',
			'max_size',
			'depot',
			'thumbnail',
		]
	)
admin.site.register(Diamond,MerchandiseAdmin,list_display=[
			'description',
			'sku',
			'carat',
			'price',
			'color',
			'clarity',
			'cut',
			'depot',
			'thumbnail',
		]
	)

admin.site.register(ColoredGem,MerchandiseAdmin,list_display=[
			'description',
			'sku',
			'carat',
			'price',
			'depot',
			'thumbnail',
		]
	)
