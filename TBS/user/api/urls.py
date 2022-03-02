from django.urls import path,re_path

from .views import PersonList,PersonDetail
from .views import EmployeeList,EmployeeDetail
from .views import CustomerList,CustomerDetail

urlpatterns = [
	path('Person/',PersonList.as_view(),name="Person_list"),
	path('Person/<int:pk>/',PersonDetail.as_view(),name="Person_detail"),

	path('Employee/',EmployeeList.as_view(),name="Employee_list"),
	path('Employee/<int:pk>/',EmployeeDetail.as_view(),name="Employee_detail"),

	path('Customer/',CustomerList.as_view(),name="Customer_list"),
	path('Customer/<int:pk>/',CustomerDetail.as_view(),name="Customer_detail"),
]