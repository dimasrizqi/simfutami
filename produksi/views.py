from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from . models import *
from .forms import *
from datetime import datetime

def listkodeproduct(request):
	var_productperpalet = product.objects.all()
	var_title = "List Kode Product"
	context = {
		'productperpalet' : var_productperpalet,
		'title' : var_title,
		}

	return render(request, 'produksi_list_kode_product.html', context)

def index(request):
	var_title = "Home"
	context = {
		'title' : var_title,
		}
	return render(request, 'index.html', context)

def history(request,product_per_palet):
	var_gudang_racking = gudangracking.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	var_detail_transisi = transisi.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	var_status_product = status_product.objects.filter(product_per_palet=product_per_palet).order_by('-update_time')#sort newert to old
	context = {
		"title"			: "Detail Lokasi & Status Product",
		"detail_transisi" : var_detail_transisi,
		"status_product" : var_status_product,
		"gudang_racking" : var_gudang_racking,
	}
	return render(request,'produksi_history.html',context)


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
		# 'pengguna'	: "3"
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
	data1 = {
		'product_per_palet'		: update_id,
		'pengguna' : pengguna_id,
	}

	statusproductform = status_product_form(request.POST or None, initial=data)
	transisi_form = transisiform(request.POST or None, initial=data1)

	if request.method == 'POST':
		if all([statusproductform.is_valid(),transisi_form.is_valid()]):
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
	#var_pengguna = pengguna.objects.get(user_id=pengguna_id)

	data = {
		'product_per_palet'		: update_id,
		'status_perpindahannya'	: "1",
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
		#"pengguna" : var_pengguna,
	}
	return render(request,'updatetransisi.html',context)

def updateproduksi(request,update_id,pengguna_id):
	data = {
		'product_per_palet'		: update_id,
		'status_perpindahannya'	: "2",
		'pengguna' : pengguna_id,
	}
	transisi_form = lokasi_product_form(request.POST or None, initial=data)

	if request.method == 'POST':
		if transisi_form.is_valid():
			transisi_form.save()
			return render(request,'ok.html')


	context = {
		"title"			: "Update Transisi Product",
		"transisi_form" : transisi_form,
		#"pengguna" : var_pengguna,
	}
	return render(request,'updatetransisi.html',context)

def createpaletindex(request):
	productperpalet_form = productperpaletform(request.POST or None)

	if request.method == 'POST':
		if productperpalet_form.is_valid():
			productperpalet_form.save()
			return redirect('/produksi/showall')

	context = {
		"title"			: "Membuat QR Code Baru",
		"productperpalet_form" : productperpalet_form,
		#"pengguna" : var_pengguna,
	}
	return render(request,'create.html',context)

def createpalet(request,pengguna_id):
	#var_pengguna = pengguna.objects.get(user_id=pengguna_id)

	data = {
		'pengguna' : pengguna_id,
	}
	productperpalet_form = productperpaletform(request.POST or None, initial=data)

	if request.method == 'POST':
		if productperpalet_form.is_valid():
			productperpalet_form.save()
			return redirect('/produksi/showall')

	context = {
		"title"			: "Membuat QR Code Baru",
		"productperpalet_form" : productperpalet_form,
		#"pengguna" : var_pengguna,
	}
	return render(request,'create.html',context)

def createproduct(request,pengguna_id):
	var_pengguna = pengguna.objects.get(user_id=pengguna_id)

	data = {
		'pengguna' : pengguna_id,
	}
	productperpalet_form = productform(request.POST or None, initial=data)

	if request.method == 'POST':
		if productperpalet_form.is_valid():
			productperpalet_form.save()
			return redirect('/produksi/showall')

	context = {
		"title"			: "Membuat Kode Product Baru",
		"productperpalet_form" : productperpalet_form,
		"pengguna" : var_pengguna,
	}
	return render(request,'create.html',context)

def createproductindex(request):
	
	productperpalet_form = productform(request.POST or None)

	if request.method == 'POST':
		if productperpalet_form.is_valid():
			productperpalet_form.save()
			return redirect('/produksi/showall')

	context = {
		"title"			: "Membuat Kode Product Baru",
		"productperpalet_form" : productperpalet_form,
	}
	return render(request,'create.html',context)

def updatewarehouse(request,update_id,pengguna_id):
	data = {
		'product_per_palet'		: update_id,
		'status_perpindahannya'	: "1",
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

def mgmt(request):
	var_title = "Home"
	var_productperpalet = productperpalet.objects.all()
	context = {
		'title' : var_title,
		'productperpalet' : var_productperpalet,
		}
	return render(request, 'mgmt.html', context)

def juser(request):
	var_release = pengguna.objects.all().values()
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

def showall(request):
	var_productperpalet = productperpalet.objects.all()
	var_title = "Hasil Produksi"
	context = {
		'productperpalet' : var_productperpalet,
		'title' : var_title,
		}

	return render(request, 'produksi_list_all.html', context)


def penggunanya(request,pengguna_id,password):
	a = pengguna.objects.get(username=pengguna_id,password=password)
	# print(pengguna_id,password)
	var_title = "Hasil Produksi"
	context = {
		'a' : a,
		'title' : var_title,
		}
	return render(request,'penggunanya.html',context)


