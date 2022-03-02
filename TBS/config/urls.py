"""TBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path,re_path

from django.conf import settings
from django.conf.urls.static import static

from user.views import EmployeeLoginView,Logout,EmployeeIndexView
from jewelry.views import JewelryListView,JewelListView,AccessoryListView,PearlListView,DiamondListView,ColoredGemListView,OtherListView
from b2c.views import OrderListView,OrderDetailView

from b2b.views import LendRecordListView


admin.site.site_header = "GEMYARD"
admin.site.site_title = "GEMYARD"
admin.site.index_title = "GEMYARD"

api_url_patterns = [
    path('jewelry/',include('jewelry.api.urls')),
    path('user/',include('user.api.urls')),
    path('core/',include('core.api.urls')),
    path('b2b/',include('b2b.api.urls')),
    path('b2c/',include('b2c.api.urls')),
]

urlpatterns = [
    path('',EmployeeIndexView.as_view()),
    path('login/',EmployeeLoginView.as_view()),
    path('logout/',Logout),
    path('salary', include('salary.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(api_url_patterns)),
    path('jewelry/Merchandise/list/',JewelryListView.as_view(),name="merchandise_list"),
    path('jewelry/Other/list/',OtherListView.as_view(),name="other_list"),
    path('jewelry/Jewel/list/',JewelListView.as_view(),name="jewel_list"),
    path('jewelry/Accessory/list/',AccessoryListView.as_view(),name="accessory_list"),
    path('jewelry/Pearl/list/',PearlListView.as_view(),name="pearl_list"),
    path('jewelry/Diamond/list/',DiamondListView.as_view(),name="diamond_list"),
    path('jewelry/ColoredGem/list/',ColoredGemListView.as_view(),name="colored_gem_list"),
    path('b2c/order/list/',OrderListView.as_view(),name="order_list"),
    path('b2c/order/<int:pk>/detail/',OrderDetailView.as_view(),name="order_detail"),
    path('b2b/lend_record/list/',LendRecordListView.as_view(),name='lend_record_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
