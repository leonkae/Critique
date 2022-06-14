import email
from rest_framework import serializers
from .models import Profile , Ratings, Reviews, Project 
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields =('pro_picture','bio','email')
        

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project        
        fields =('image','projectname','description', 'urls')
    
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    project = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields =('id', 'urls', 'profile', 'project')       