from django.urls import path,re_path

from .api_views import PackageList,PackageDetail
from .api_views import AreaList,AreaDetail
from .api_views import AddressList,AddressDetail
from .api_views import PayList,PayDetail

urlpatterns = [
	path('Package/',PackageList.as_view(),name="Package_list"),
	path('Package/<int:pk>/',PackageDetail.as_view(),name="Package_detail"),

	path('Area/',AreaList.as_view(),name="Area_list"),
	path('Area/<int:pk>/',AreaDetail.as_view(),name="Area_detail"),

	path('Address/',AddressList.as_view(),name="Address_list"),
	path('Address/<int:pk>/',AddressDetail.as_view(),name="Address_detail"),

	path('Pay/',PayList.as_view(),name="Pay_list"),
	path('Pay/<int:pk>/',PayDetail.as_view(),name="Pay_detail"),
]