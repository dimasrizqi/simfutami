from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from . models import *
from .forms import *

def detailtransisi(request,product_per_palet):
	var_gudang_racking = gudangracking.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	var_detail_transisi = transisi.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	var_status_product = status_product.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	context = {
		"title"			: "Detail Lokasi & Status Product",
		"detail_transisi" : var_detail_transisi,
		"status_product" : var_status_product,
		"gudang_racking" : var_gudang_racking,
	}
	return render(request,'detail_transisi.html',context)


def updatetransisi(request,update_id):
	# inin coba coba 
	data = {
		'product_per_palet'		: update_id
	}

	transisi_form = transisiform(request.POST or None, initial=data)
	if request.method == 'POST':
		if transisi_form.is_valid():
			transisi_form.save()

	print(transisi_form)
	context = {
		"title"			: "Update Transisi Product",
		"transisi_form" : transisi_form,
	}
	return render(request,'updatetransisi.html',context)

def updatestatus(request,update_id):
	data = {
		'product_per_palet'		: update_id,
	}

	statusproductform = status_product_form(request.POST or None, initial=data)
	if request.method == 'POST':
		if statusproductform.is_valid():
			statusproductform.save()
			return render(request,'ok.html')

	context = {
		"title"			: "Update Status Product",
		"statusproductform" : statusproductform,
	}
	return render(request,'update_status.html',context)
	
def updateqc(request,update_id,pengguna_id):
	data = {
		'product_per_palet'		: update_id,
		'pengguna' : pengguna_id,
	}
	statusproductform = status_product_form(request.POST or None, initial=data)
	transisi_form = transisiform(request.POST or None, initial=data)
	if request.method == 'POST':
		if all([transisi_form.is_valid(),statusproductform.is_valid()]):
			transisi_form.save()
			statusproductform.save()
			return render(request,'ok.html')

	context = {
		"title"			: "Update Status Product",
		"transisi_form" : transisi_form,
		"statusproductform" : statusproductform,
	}
	return render(request,'updateqc.html',context)

def updateforklip(request,update_id,pengguna_id):
	var_pengguna = pengguna.objects.get(user_id=pengguna_id)

	data = {
		'product_per_palet'		: update_id,
		'status_perpindahan'	: "GUDANG HCI",
		'pengguna' : pengguna_id,
	}
	transisi_form = transisiform(request.POST or None, initial=data)

	if request.method == 'POST':
		if transisi_form.is_valid():
			transisi_form.save()
			return render(request,'ok.html')


	context = {
		"title"			: "Update Transisi Product",
		"transisi_form" : transisi_form,
		"pengguna" : var_pengguna,
	}
	return render(request,'updatetransisi.html',context)

def createpalet(request,pengguna_id):
	var_pengguna = pengguna.objects.get(user_id=pengguna_id)

	data = {
		'pengguna' : pengguna_id,
	}
	productperpalet_form = productperpaletform(request.POST or None, initial=data)

	if request.method == 'POST':
		if productperpalet_form.is_valid():
			productperpalet_form.save()
			return render(request,'ok.html')

	context = {
		"title"			: "Membuat Palet Baru",
		"productperpalet_form" : productperpalet_form,
		"pengguna" : var_pengguna,
	}
	return render(request,'create_palet.html',context)


def updatewarehouse(request,update_id,pengguna_id):
	data = {
		'product_per_palet'		: update_id,
		'status_perpindahan'	: "GUDANG RACKING",
		'pengguna' : pengguna_id
		}

	transisi_form = transisiform(request.POST or None, initial=data)
	gudangracking_form = gudangrackingform(request.POST or None, initial=data)
	if request.method == 'POST':
		if all([transisi_form.is_valid(),gudangracking_form.is_valid()]):
		#if transisi_form.is_valid():
			transisi_form.save()
			gudangracking_form.save()
			return render(request,'ok.html')

	context = {
		"title"			: "Penyimpanan Gudang Racking",
		"transisi_form" : transisi_form,
		"gudangracking_form" : gudangracking_form,
	}
	return render(request,'updategudangracking.html',context)

# Create your views here.
def index(request):
	var_title = "Home"
	var_release = Release.objects.all()
	return render(request, 'index.html', {
		'title' : var_title,
		'release' : var_release,
		})


def juser(request):
	var_release = user.objects.all().values()
	var_release_list = list(var_release)
	return JsonResponse(var_release_list, safe=False)

def json(request):
	var_release = Release.objects.all().values()
	var_release_list = list(var_release)
	return JsonResponse(var_release_list, safe=False)
	# context = {
	# 	# 'title':'judulnya JSON',
	# 	'id_user' : '1',	
	# }
	# return JsonResponse(context)

def palet(request,productperpalet_id):
	var_productperpalet = productperpalet.objects.filter(productperpalet_id=productperpalet_id)
	var_title = "Detail Produksi Perpalet"
	context = {
		'productperpalet' : var_productperpalet,
		'title' : var_title,
		}

	return render(request, 'show_perpalet.html', context)

