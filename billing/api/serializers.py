from rest_framework import serializers
import payment.models

class ScannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = payment.models.Scanner
		fields = '__all__'

class ProductGroupSerializer(serializers.ModelSerializer):
	scanners = ScannerSerializer(read_only=True, many=True)
	class Meta:
		model = payment.models.ProductGroup
		fields = '__all__'


class AccountConnectorGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = payment.models.AccountConnectorGroup
		fields = '__all__'

class ScannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = payment.models.Scanner
		fields = '__all__'

class PaymentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = payment.models.PaymentList
		fields = '__all__'