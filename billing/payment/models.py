import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class BasePaymentInfo(models.Model):
	name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('name'))
	price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('price'))
	available = models.BooleanField(default=True, verbose_name=_('Whether product available'))
	created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('creation time'))

	class Meta:
		abstract = True

class Product(BasePaymentInfo):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	country = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Product country'))

	def __str__(self):
		return self.name

class AccountConnector(BasePaymentInfo):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	description = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Account description'))

	def __str__(self):
		return self.name

class Scanner(models.Model):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	scanned_number_of_times = models.IntegerField(default=0)

	def __str__(self):
		return str(self.scanned_number_of_times)

class PaymentGroup(models.Model):
	count = models.IntegerField(default=0)
	discount_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Discount price'))
	available = models.BooleanField(default=True, verbose_name=_('Whether group is available available'))

	class Meta:
		abstract = True	

class ProductGroup(PaymentGroup):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	product = models.ForeignKey(Product, verbose_name='Related product')
	scanners = models.ManyToManyField(Scanner, verbose_name='Related scanner')

	def __str__(self):
		scanners = [str(sc) for sc in self.scanners.all()]
		return str(self.product) + ' - ' + str(scanners)

class AccountConnectorGroup(PaymentGroup):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	account = models.ForeignKey(AccountConnector, verbose_name='Related account connector')

	def __str__(self):
		return str(self.account)

class PaymentList(models.Model):
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, verbose_name=_('identifier'))
	total_price   = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Total price'))
	product_group = models.ForeignKey(ProductGroup, verbose_name='product group')
	account_group = models.ForeignKey(AccountConnectorGroup, verbose_name='account group')