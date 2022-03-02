from django.urls import path,re_path

from .views import JewelryListView,JewelListView,AccessoryListView,PearlListView,DiamondListView,ColoredGemListView,OtherListView



urlpatterns = [
	path('Merchandise/list/',JewelryListView.as_view(),name="merchandise_list"),
    path('Other/list/',OtherListView.as_view(),name="other_list"),
    path('Jewel/list/',JewelListView.as_view(),name="jewel_list"),
    path('Accessory/list/',AccessoryListView.as_view(),name="accessory_list"),
    path('Pearl/list/',PearlListView.as_view(),name="pearl_list"),
    path('Diamond/list/',DiamondListView.as_view(),name="diamond_list"),
    path('ColoredGem/list/',ColoredGemListView.as_view(),name="colored_gem_list"),
]