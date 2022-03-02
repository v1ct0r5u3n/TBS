from django.urls import path,re_path

from .views import B2BRecordList,B2BRecordDetail
from .views import B2BConfirmList,B2BConfirmDetail

urlpatterns = [
	path('B2BRecord/',B2BRecordList.as_view(),name="B2BRecord_list"),
	path('B2BRecord/<int:pk>/',B2BRecordDetail.as_view(),name="B2BRecord_detail"),

	path('B2BConfirm/',B2BConfirmList.as_view(),name="B2BConfirm_list"),
	path('B2BConfirm/<int:pk>/',B2BConfirmDetail.as_view(),name="B2BConfirm_detail"),
]