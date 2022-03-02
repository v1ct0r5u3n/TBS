from rest_framework import serializers
from  b2b.models import B2BRecord,B2BConfirm

class B2BRecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = B2BRecord
		fields = '__all__'

class B2BConfirmSerializer(serializers.ModelSerializer):
	class Meta:
		model = B2BConfirm
		fields = '__all__'
