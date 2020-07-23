from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'hunter_game/home.html')

def guidelines(request):
	return render(request,'hunter_game/guidelines.html')

def about(request):
	return render(request,'hunter_game/about.html')

def scoreboard(request):
	return render(request,'hunter_game/scoreboard.html')

def notification(request):
	return render(request,'hunter_game/notification.html')

def events(request):
	return render(request,'hunter_game/events.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}')
			return redirect('login')
			
	else:
		form = UserRegisterForm()
	return render(request,'hunter_game/register.html',{'form' : form})

@login_required
def profile(request):
    return render(request, 'hunter_game/profile.html')
