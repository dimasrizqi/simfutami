from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from . models import *
from datetime import datetime

def index(request):
	var_title = "Home"
	context = {
		'title' : var_title,
		}
	return render(request, 'index.html', context)
