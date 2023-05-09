from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
#class UsuarioView(

def home(request):

	return render(request, './home.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('Home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'templates/register.html', context)