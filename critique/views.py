from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    return render(request,'critiques/home.html')

def signup(request):
    ''' signup view '''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form= CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                created_user = form.save()
                Profile.objects.get_or_create(user=created_user)
                messages.success(request, 'Account for' + username + 'created succesfully')
                return redirect('login')   
             
    context ={'form': form}
    return render(request, 'critiques/signup.html', context)

def login_page(request):
    '''login view'''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            print(username,password,user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Check username or password !')
        return render(request,'critiques/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')