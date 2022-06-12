from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('addprofile/',views.addprofile, name='addprofile'),
    path('profile/', views.profile, name='profile'),
    path('create/',views.create, name='create'),
    path('search/', views.search, name='search' ),
    path('review/<str:pk>/', views.review, name='review'),
    path('like/<int:pk>/,', views.like, name='like'),
    
]

