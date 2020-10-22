from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import BSCS

def index(request):
	return render(request,'index.html')


def register(request):
    form =  createuserform()
    if request.method == 'POST':
    	form = createuserform(request.POST)
    	if form.is_valid():
    		form.save()
    		username = form.cleaned_data.get('username')
    		messages.success(request,'Account Created for '+username)
    		return redirect('login')

    context = {'form':form}
    print (context)
    return render(request, 'register.html',context)



def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


@login_required(login_url='login')
def home(request):
	all_data = BSCS.objects.all()
	context = {"DATA":all_data}
	return render(request, 'home.html', context)



def logOut(request):
	auth_logout(request)
	return redirect('login')



def contactus(request):
	return render(request, 'contactus.html')









