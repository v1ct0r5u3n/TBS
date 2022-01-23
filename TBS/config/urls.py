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
from jewelry.views import JewelryListView


admin.site.site_header = "GEMYARD"
admin.site.site_title = "GEMYARD"
admin.site.index_title = "GEMYARD"

api_url_patterns = [
    path('jewelry/',include('jewelry.urls')),
    path('user/',include('user.urls')),
    path('core/',include('core.urls')),
    path('b2b/',include('b2b.urls')),
    path('b2c/',include('b2c.urls')),
]

urlpatterns = [
    path('',EmployeeIndexView.as_view()),
    path('login/',EmployeeLoginView.as_view()),
    path('logout/',Logout),
    path('salary', include('salary.urls')),
    path('admin/', admin.site.urls),
    path('jewelry/Merchandise/list/',JewelryListView.as_view(),name="merchandise_list"),
    path('api/',include(api_url_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
