from django.contrib import admin

# Register your models here.
from .models import Depot,Jewel,Accessory,Pearl,Diamond

admin.site.register(Depot)
admin.site.register(Jewel)
admin.site.register(Accessory)
admin.site.register(Pearl)
admin.site.register(Diamond)
