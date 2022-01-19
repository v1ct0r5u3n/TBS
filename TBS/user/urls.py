from django.urls import path,re_path

from .api_views import PersonList,PersonDetail
from .api_views import EmployeeList,EmployeeDetail
from .api_views import CustomerList,CustomerDetail

urlpatterns = [
	path('Person/',PersonList.as_view(),name="Person_list"),
	path('Person/<int:pk>/',PersonDetail.as_view(),name="Person_detail"),

	path('Employee/',EmployeeList.as_view(),name="Employee_list"),
	path('Employee/<int:pk>/',EmployeeDetail.as_view(),name="Employee_detail"),

	path('Customer/',CustomerList.as_view(),name="Customer_list"),
	path('Customer/<int:pk>/',CustomerDetail.as_view(),name="Customer_detail"),
]