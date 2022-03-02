from django.urls import path,re_path

from .views import LendRecordListView

urlpatterns = [
	path('lend_record/list/',LendRecordListView.as_view(),name='lend_record_list'),
]