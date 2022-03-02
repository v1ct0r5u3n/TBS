from django.urls import path,re_path

from .views import OrderList,OrderDetail
from .views import SalesShareList,SalesShareDetail
from .views import RefundList,RefundDetail

urlpatterns = [
	path('Order/',OrderList.as_view(),name="Order_list"),
	path('Order/<int:pk>/',OrderDetail.as_view(),name="Order_detail"),

	path('SalesShare/',SalesShareList.as_view(),name="SalesShare_list"),
	path('SalesShare/<int:pk>/',SalesShareDetail.as_view(),name="SalesShare_detail"),

	path('Refund/',RefundList.as_view(),name="Refund_list"),
	path('Refund/<int:pk>/',RefundDetail.as_view(),name="Refund_detail"),
]