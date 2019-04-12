from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^json$', views.juser),
	url(r'^mgmt$', views.mgmt),
	url(r'^showall$', views.showall),
	url(r'^showproduct$', views.listkodeproduct),
	url(r'^createpalet$', views.createpaletindex), 
	url(r'^createproduct$', views.createproductindex),
	url(r'^palet/(?P<productperpalet_id>[0-9]+)$', views.palet), #jangna di hapus ajib ini
	url(r'^createpalet/(?P<pengguna_id>([0-9]+))$', views.createpalet), 
	url(r'^createproduct/(?P<pengguna_id>([0-9]+))$', views.createproduct), 
	url(r'^qc/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updateqc), 
	url(r'^warehouse/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updatewarehouse), 
	url(r'^forklip/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updateforklip), 
	url(r'^produksi/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updateproduksi),
	url(r'^penggunanya/(?P<pengguna_id>([\w]+))-(?P<password>([\w]+))$', views.penggunanya),
	url(r'^update/(?P<update_id>[0-9]+)$', views.updatetransisi), 
	url(r'^updatestatus/(?P<update_id>[0-9]+)$', views.updatestatus), 
	url(r'^history/(?P<product_per_palet>[0-9]+)$', views.history), 

]