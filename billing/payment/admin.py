from django.contrib import admin

# Register your models here.
from .models import Product, AccountConnector, Scanner, ProductGroup, AccountConnectorGroup, PaymentList

admin.site.register(Product)
admin.site.register(AccountConnector)
admin.site.register(Scanner)
admin.site.register(ProductGroup)
admin.site.register(AccountConnectorGroup)
admin.site.register(PaymentList)