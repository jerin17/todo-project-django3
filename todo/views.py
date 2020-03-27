from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

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