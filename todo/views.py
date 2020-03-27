from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
	return render(request, 'todo/home.html')


def signup(request):
	if request.method == 'GET':
		return render(request, 'todo/signup.html',{'form':UserCreationForm()})

	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request,user)
				return redirect('current')

			except IntegrityError:
				return render(request, 'todo/signup.html',{'form':UserCreationForm(),'error':"Username already exists."})				

		else:
			return render(request, 'todo/signup.html',{'form':UserCreationForm(),'error':"passwords did not match."})


def current(request):
	return render(request, 'todo/current.html')

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'todo/login.html',{'form':AuthenticationForm()})

	else:
		user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
		if user is None:
			return render(request, 'todo/login.html',{'form':AuthenticationForm(), 'error':'username or password did not match !'})
		else:
			login(request,user)
			return redirect('current')

def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')