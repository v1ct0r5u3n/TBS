from django.urls import path,re_path

from .api_views import DepotList,DepotDetail
from .api_views import CertificateList,CertificateDetail
from .api_views import PriceCategoryList,PriceCategoryDetail
from .api_views import RecordList,RecordDetail,MerchandiseRecordList,MerchandiseRecordDetail,RecordPayList,RecordPayDetail
from .api_views import SkuList,SkuDetail,MerchandiseList,MerchandiseDetail
from .api_views import JewelList,JewelDetail,AccessoryList,AccessoryDetail
from .api_views import GemList,GemDetail,PearlList,PearlDetail,DiamondList,DiamondDetail,ColoredGemList,ColoredGemDetail

'''
from django.views.decorators.http import require_http_methods
from .models import Jewel
from django.http import HttpResponse
def add_100_jewel(request):
	jewel = Jewel.objects.first()
	i = 100
	while i>0:
		jewel.pk = None
		jewel.id = None
		jewel.save()
		i-=1
			
	return HttpResponse(Jewel.objects.all().count())
'''

urlpatterns = [
#	path('add_100_jewel/',add_100_jewel),
	path('Depot/',DepotList.as_view(),name="depot_list"),
	path('Depot/<int:pk>/',DepotDetail.as_view(),name="depot_detail"),

	path('Certificate/',CertificateList.as_view(),name="Certificate_list"),
	path('Certificate/<int:pk>/',CertificateDetail.as_view(),name="Certificate_detail"),

	path('PriceCategory/',PriceCategoryList.as_view(),name="PriceCategory_list"),
	path('PriceCategory/<int:pk>/',PriceCategoryDetail.as_view(),name="PriceCategory_detail"),

	path('Record/',RecordList.as_view(),name="Record_list"),
	path('Record/<int:pk>/',RecordDetail.as_view(),name="Record_detail"),

	path('MerchandiseRecord/',MerchandiseRecordList.as_view(),name="MerchandiseRecord_list"),
	path('MerchandiseRecord/<int:pk>/',MerchandiseRecordDetail.as_view(),name="MerchandiseRecord_detail"),

	path('RecordPay/',RecordPayList.as_view(),name="RecordPay_list"),
	path('RecordPay/<int:pk>/',RecordPayDetail.as_view(),name="RecordPay_detail"),

	path('Sku/',SkuList.as_view(),name="Sku_list"),
	path('Sku/<int:pk>/',SkuDetail.as_view(),name="Sku_detail"),

	path('Merchandise/',MerchandiseList.as_view(),name="Merchandise_list"),
	path('Merchandise/<int:pk>/',MerchandiseDetail.as_view(),name="Merchandise_detail"),

	path('Merchandise/Jewel/',JewelList.as_view(),name="jewel_list"),
	path('Merchandise/Jewel/<int:pk>/',JewelDetail.as_view(),name="jewel_detail"),

	path('Merchandise/Accessory/',AccessoryList.as_view(),name="Accessory_list"),
	path('Merchandise/Accessory/<int:pk>/',AccessoryDetail.as_view(),name="Accessory_detail"),

	path('Merchandise/Gem/',GemList.as_view(),name="Gem_list"),
	path('Merchandise/Gem/<int:pk>/',GemDetail.as_view(),name="Gem_detail"),

	path('Merchandise/Gem/Pearl/',PearlList.as_view(),name="Pearl_list"),
	path('Merchandise/Gem/Pearl/<int:pk>/',PearlDetail.as_view(),name="Pearl_detail"),

	path('Merchandise/Gem/Diamond/',DiamondList.as_view(),name="Diamond_list"),
	path('Merchandise/Gem/Diamond/<int:pk>/',DiamondDetail.as_view(),name="Diamond_detail"),

	path('Merchandise/Gem/ColoredGem/',ColoredGemList.as_view(),name="ColoredGem_list"),
	path('Merchandise/Gem/ColoredGem/<int:pk>/',ColoredGemDetail.as_view(),name="ColoredGem_detail"),
]