from rest_framework import serializers

from b2c.models import Order,SalesShare
from b2c.models import Refund


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'

class SalesShareSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalesShare
		fields = '__all__'

class RefundSerializer(serializers.ModelSerializer):
	class Meta:
		model = Refund
		fields = '__all__'
