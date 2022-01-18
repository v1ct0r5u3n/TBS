from django.urls import path,re_path

from .api_views import DepotList,DepotDetail
from .api_views import CertificateList,CertificateDetail
from .api_views import PriceCategoryList,PriceCategoryDetail
from .api_views import RecordList,RecordDetail,MerchandiseRecordList,MerchandiseRecordDetail,RecordPayList,RecordPayDetail
from .api_views import SkuList,SkuDetail,MerchandiseList,MerchandiseDetail
from .api_views import JewelList,JewelDetail,AccessoryList,AccessoryDetail
from .api_views import GemList,GemDetail,PearlList,PearlDetail,DiamondList,DiamondDetail,ColoredGemList,ColoredGemDetail

urlpatterns = [
	path('Depot/',DepotList.as_view(),name="depot_list"),
	path('Depot/<pk>/',DepotDetail.as_view(),name="depot_detail"),

	path('Certificate/',CertificateList.as_view(),name="Certificate_list"),
	path('Certificate/<pk>/',CertificateDetail.as_view(),name="Certificate_detail"),

	path('PriceCategory/',PriceCategoryList.as_view(),name="PriceCategory_list"),
	path('PriceCategory/<pk>/',PriceCategoryDetail.as_view(),name="PriceCategory_detail"),

	path('Record/',RecordList.as_view(),name="Record_list"),
	path('Record/<pk>/',RecordDetail.as_view(),name="Record_detail"),

	path('MerchandiseRecord/',MerchandiseRecordList.as_view(),name="MerchandiseRecord_list"),
	path('MerchandiseRecord/<pk>/',MerchandiseRecordDetail.as_view(),name="MerchandiseRecord_detail"),

	path('RecordPay/',RecordPayList.as_view(),name="RecordPay_list"),
	path('RecordPay/<pk>/',RecordPayDetail.as_view(),name="RecordPay_detail"),

	path('Sku/',SkuList.as_view(),name="Sku_list"),
	path('Sku/<pk>/',SkuDetail.as_view(),name="Sku_detail"),

	path('Merchandise/',MerchandiseList.as_view(),name="Merchandise_list"),
	path('Merchandise/<pk>/',MerchandiseDetail.as_view(),name="Merchandise_detail"),

	path('Merchandise/Jewel/',JewelList.as_view(),name="jewel_list"),
	path('Merchandise/Jewel/<pk>/',JewelDetail.as_view(),name="jewel_detail"),

	path('Merchandise/Accessory/',AccessoryList.as_view(),name="Accessory_list"),
	path('Merchandise/Accessory/<pk>/',AccessoryDetail.as_view(),name="Accessory_detail"),

	path('Merchandise/Gem/',GemList.as_view(),name="Gem_list"),
	path('Merchandise/Gem/<pk>/',GemDetail.as_view(),name="Gem_detail"),

	path('Merchandise/Gem/Pearl/',PearlList.as_view(),name="Pearl_list"),
	path('Merchandise/Gem/Pearl/<pk>/',PearlDetail.as_view(),name="Pearl_detail"),

	path('Merchandise/Gem/Diamond/',DiamondList.as_view(),name="Diamond_list"),
	path('Merchandise/Gem/Diamond/<pk>/',DiamondDetail.as_view(),name="Diamond_detail"),

	path('Merchandise/Gem/ColoredGem/',ColoredGemList.as_view(),name="ColoredGem_list"),
	path('Merchandise/Gem/ColoredGem/<pk>/',ColoredGemDetail.as_view(),name="ColoredGem_detail"),
]