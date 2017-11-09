from rest_framework import exceptions
from rest_framework import viewsets


import payment.models
from . import serializers

class ProductGroup(viewsets.ModelViewSet):
    queryset = payment.models.ProductGroup.objects.all() # add select related
    serializer_class = serializers.ProductGroupSerializer

class AccountGroup(viewsets.ModelViewSet):
	queryset = payment.models.AccountConnectorGroup.objects.all()
	serializer_class = serializers.AccountConnectorGroupSerializer

class Scanner(viewsets.ModelViewSet):
	queryset = payment.models.Scanner.objects.all()
	serializer_class = serializers.ScannerSerializer

class Payment(viewsets.ModelViewSet):
	queryset = payment.models.PaymentList.objects.all()
	serializer_class = serializers.PaymentListSerializer