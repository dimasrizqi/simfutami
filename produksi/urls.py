from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^json$', views.json),
	url(r'^showall$', views.showall),
	#url(r'^(?P<produksi_id>[0-9]+)$', views.release),
	url(r'^palet/(?P<productperpalet_id>[0-9]+)$', views.palet), #jangna di hapus ajib ini
	url(r'^createpalet/(?P<pengguna_id>([0-9]+))$', views.createpalet), 
	url(r'^createproduct/(?P<pengguna_id>([0-9]+))$', views.createproduct), 
	url(r'^qc/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updateqc), 
	url(r'^warehouse/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updatewarehouse), 
	url(r'^forklip/(?P<update_id>[0-9]+)-(?P<pengguna_id>([0-9]+))$', views.updateforklip), 
	url(r'^update/(?P<update_id>[0-9]+)$', views.updatetransisi), 
	url(r'^updatestatus/(?P<update_id>[0-9]+)$', views.updatestatus), 
	url(r'^perpindahanproduct/(?P<product_per_palet>[0-9]+)$', views.detailtransisi), 

]