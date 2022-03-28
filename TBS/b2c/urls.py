from django.urls import path,re_path

from .views import OrderListView,OrderDetailView,CreateOrderView

urlpatterns = [
	path('order/list/',OrderListView.as_view(),name="order_list"),
    path('order/<int:pk>/detail/',OrderDetailView.as_view(),name="order_detail"),
    path('order/create/',CreateOrderView.as_view(),name="order_create"),
]