from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.contrib.auth import logout

def index(request):
	var_title = "Home"
	context = {
		'title' : var_title,
		}
	return render(request, 'login.html', context)

# def logout(request):
# 	logout(request)
# 	return redirect('/login')
	