from rest_framework import serializers
from .models import Depot
from .models import Certificate
from .models import PriceCategory
from .models import Record,MerchandiseRecord,RecordPay
from .models import Sku,Merchandise
from .models import Jewel,Accessory
from .models import Gem,Pearl,Diamond,ColoredGem

class DepotSerializer(serializers.ModelSerializer):
	class Meta:
		model = Depot
		fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		fields = '__all__'

class PriceCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = PriceCategory
		fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Record
		fields = '__all__'

class MerchandiseRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = MerchandiseRecord
		fields = '__all__'

class RecordPaySerializer(serializers.ModelSerializer):
	class Meta:
		model = RecordPay
		fields = '__all__'

class SkuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sku
		fields = '__all__'
		
class MerchandiseSerializer(serializers.ModelSerializer):
	certificate = CertificateSerializer(many=True,read_only=True,required=False)
	class Meta:
		model = Merchandise
		fields = '__all__'

class JewelSerializer(MerchandiseSerializer):
	class Meta:
		model = Jewel
		fields = '__all__'

class AccessorySerializer(MerchandiseSerializer):
	class Meta:
		model = Accessory
		fields = '__all__'

class GemSerializer(MerchandiseSerializer):
	class Meta:
		model = Gem
		fields = '__all__'

class PearlSerializer(MerchandiseSerializer):
	class Meta:
		model = Pearl
		fields = '__all__'

class DiamondSerializer(MerchandiseSerializer):
	class Meta:
		model = Diamond
		fields = '__all__'

class ColoredGemSerializer(MerchandiseSerializer):
	class Meta:
		model = ColoredGem
		fields = '__all__'