from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?i)products/$', views.ProductGroup.as_view(actions={'get': 'list'}, suffix='List'), name='product-list'),
    url(r'^(?i)accounts/$', views.AccountGroup.as_view(actions={'get': 'list'}, suffix='List'), name='account-list'),
    url(r'^(?i)scanners/$', views.Scanner.as_view(actions={'get': 'list'}, suffix='List'), name='scanner-list'),
    url(r'^(?i)payment/$', views.Payment.as_view(actions={'get': 'list', 'post' : 'create'}, suffix='List'), name='payment-list'), # create call
    url(r'^(?i)payment/(?P<pk>[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$', views.Payment.as_view(actions={'get': 'retrieve', 'put': 'update'}, suffix='List'), name='payment-detail'), #
]
