from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse("<h1>halaman home inventory</h1>")
	
def it(request):
	return HttpResponse("<h1>halaman it inventory</h1>")

# Create your views here.
