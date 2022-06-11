from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
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
                return redirect('home')   
             
    context ={'form': form}
    return render(request, 'critiques/signup.html', context)
