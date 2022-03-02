from rest_framework import serializers

from core.models import Package
from core.models import Area,Address
from core.models import Pay

class PackageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Package
		fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Area
		fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'

class PaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Pay
		fields = '__all__'
