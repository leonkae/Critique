from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from .models import Reviews as ReviewsModel
from .models import *

# Create your views here.

def home(request):
    '''home view''' 
    images=Project.objects.order_by("-created").all()
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    
    return render(request,'critiques/home.html', {'images':images, 'user_profile':user_profile})

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
    
def viewproject(request,pk):
    images = Project.objects.get(id=pk)
    return render(request,'critiques/photo.html',{'images':images})

@login_required(login_url='login') 
def logout_user(request):
    '''logout view'''
    logout(request)
    return redirect('login')

@login_required(login_url='login') 
def addprofile(request):
    '''update view'''
    current_user=request.user
    
    if request.method == 'POST':
        pro_picture = request.FILES.get('pro_picture')
        profile = Profile.objects.get(user__id=request.user.id)
        profile.bio = request.POST['bio']
        profile.pro_picture = pro_picture
        profile.save()
    return render(request,'critiques/addprofile.html')

@login_required(login_url='login') 
def profile(request):
    '''profile view'''
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    images = Project.objects.order_by("-created").filter(profile__user=request.user)
    image_length =(len(images))
    
    return render(request,'critiques/profile.html',{'user_profile':user_profile, 'images':images,'image_length':image_length})


@login_required(login_url='login') 
def create(request):
    '''submit projec view'''
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    
    if request.method == 'POST':
        data = request.POST
        image =request.FILES.get('image')
        print('data',data)
        print('image', image)
        
        project = Project.objects.create(
            image = image,
            projectname = data['projectname'],
            description = data['description'],
            profile = user_profile,
            urls = data['urls'],
        )
        project.save()
        return redirect('home')
    return render(request, 'critiques/create.html')


def search(request):
    '''search view'''
    if request.method == "POST":
        searched = request.POST['searched']
        searched_object = Project.objects.filter(profile__user__username__icontains=searched)
        
    return render(request, 'critiques/search.html',{'searched_object':searched_object}) 
    

@login_required(login_url='login') 
def review(request,pk):
    '''post review view'''
    
    if request.method =='POST':
        data=request.POST
        
        project = Project.objects.get(pk=pk)
        new_review = ReviewsModel.objects.create(
            user=request.user,
            text=request.POST['review'],
            user_post = project, 
        )
        project.reviews.add(new_review)
        project.save()
        return redirect('home')
    
    return render(request, 'critiques/review.html')


@login_required(login_url='login') 
def like(request, pk):
    '''like/star view'''
    if request.method == 'POST':
        project = get_object_or_404(Project, id=pk)    
        project.likes.add(request.user)
        print(project)
        
        return HttpResponseRedirect(reverse('home'))
    return redirect('home')