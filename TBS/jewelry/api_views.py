from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Depot
from .models import Certificate
from .models import PriceCategory
from .models import Record,MerchandiseRecord,RecordPay
from .models import Sku,Merchandise
from .models import Jewel,Accessory
from .models import Gem,Pearl,Diamond,ColoredGem

from .serializers import DepotSerializer
from .serializers import CertificateSerializer
from .serializers import PriceCategorySerializer
from .serializers import RecordSerializer,MerchandiseRecordSerializer,RecordPaySerializer
from .serializers import SkuSerializer,MerchandiseSerializer
from .serializers import JewelSerializer,AccessorySerializer
from .serializers import GemSerializer,PearlSerializer,DiamondSerializer,ColoredGemSerializer
# Create your views here.

class DepotList(generics.ListCreateAPIView):
	queryset = Depot.objects.all()
	serializer_class = DepotSerializer

class DepotDetail(generics.RetrieveDestroyAPIView):
	queryset = Depot.objects.all()
	serializer_class = DepotSerializer

class CertificateList(generics.ListCreateAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class CertificateDetail(generics.RetrieveDestroyAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class PriceCategoryList(generics.ListCreateAPIView):
	queryset = PriceCategory.objects.all()
	serializer_class = PriceCategorySerializer

class PriceCategoryDetail(generics.RetrieveDestroyAPIView):
	queryset = PriceCategory.objects.all()
	serializer_class = PriceCategorySerializer

class RecordList(generics.ListCreateAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveDestroyAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer

class MerchandiseRecordList(generics.ListCreateAPIView):
	queryset = MerchandiseRecord.objects.all()
	serializer_class = MerchandiseRecordSerializer

class MerchandiseRecordDetail(generics.RetrieveDestroyAPIView):
	queryset = MerchandiseRecord.objects.all()
	serializer_class = MerchandiseRecordSerializer

class RecordPayList(generics.ListCreateAPIView):
	queryset = RecordPay.objects.all()
	serializer_class = RecordPaySerializer

class RecordPayDetail(generics.RetrieveDestroyAPIView):
	queryset = RecordPay.objects.all()
	serializer_class = RecordPaySerializer

class SkuList(generics.ListCreateAPIView):
	queryset = Sku.objects.all()
	serializer_class = SkuSerializer

class SkuDetail(generics.RetrieveDestroyAPIView):
	queryset = Sku.objects.all()
	serializer_class = SkuSerializer

class MerchandiseList(generics.ListCreateAPIView):
	queryset = Merchandise.objects.all()
	serializer_class = MerchandiseSerializer

class MerchandiseDetail(generics.RetrieveDestroyAPIView):
	queryset = Merchandise.objects.all()
	serializer_class = MerchandiseSerializer

class JewelList(generics.ListCreateAPIView):
	queryset = Jewel.objects.all()
	serializer_class = JewelSerializer

class JewelDetail(generics.RetrieveDestroyAPIView):
	queryset = Jewel.objects.all()
	serializer_class = JewelSerializer

class AccessoryList(generics.ListCreateAPIView):
	queryset = Accessory.objects.all()
	serializer_class = AccessorySerializer

class AccessoryDetail(generics.RetrieveDestroyAPIView):
	queryset = Accessory.objects.all()
	serializer_class = AccessorySerializer

class GemList(generics.ListCreateAPIView):
	queryset = Gem.objects.all()
	serializer_class = GemSerializer

class GemDetail(generics.RetrieveDestroyAPIView):
	queryset = Gem.objects.all()
	serializer_class = GemSerializer

class PearlList(generics.ListCreateAPIView):
	queryset = Pearl.objects.all()
	serializer_class = PearlSerializer

class PearlDetail(generics.RetrieveDestroyAPIView):
	queryset = Pearl.objects.all()
	serializer_class = PearlSerializer

class DiamondList(generics.ListCreateAPIView):
	queryset = Diamond.objects.all()
	serializer_class = DiamondSerializer

class DiamondDetail(generics.RetrieveDestroyAPIView):
	queryset = Diamond.objects.all()
	serializer_class = DiamondSerializer

class ColoredGemList(generics.ListCreateAPIView):
	queryset = ColoredGem.objects.all()
	serializer_class = ColoredGemSerializer

class ColoredGemDetail(generics.RetrieveDestroyAPIView):
	queryset = ColoredGem.objects.all()
	serializer_class = ColoredGemSerializer