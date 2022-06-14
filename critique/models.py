from cgitb import text
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    '''profile model'''
    pro_picture =models.ImageField(upload_to ='profile/', default='')
    bio = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    email= models.EmailField(blank=True)
    
    
    def __str__(self):
        return self.user.username
    
    
class Ratings(models.Model):
    design = models.IntegerField(choices=list(zip(range(1, 100), range(1, 100))), blank=True)
    usability =models.IntegerField(choices=list(zip(range(1, 100), range(1,100))), blank=True)
    content =models.IntegerField(choices= list(zip(range(1, 100), range(1, 100))), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
    design_percent =models.FloatField(default=0)
    usability_percent= models.FloatField(default=0)
    content_average =models.FloatField(default=0)   
    average =models.FloatField(default=0) 
    rev =models.ForeignKey('Reviews', on_delete=models.CASCADE,related_name='reviews')
    
    
    
    def _str__(self):
        return self.name
    
    
    
    
    
class Reviews(models.Model):
    '''reviews model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
    user_post =models.ForeignKey('Project', on_delete=models.CASCADE, related_name='user_reviews')
    
    
    
    def __str__(self):
        return f' {self.user.username} Image'
    


class Project(models.Model):
    '''project model'''
    
    image = models.ImageField(upload_to='media/', default='image.png')
    projectname =models.CharField(max_length=100)
    description=models.CharField(max_length=255, null=False, blank=False)
    likes =models.ManyToManyField(User, related_name='critique_image')
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
    reviews =models.ManyToManyField('Reviews',blank=True)
    urls = models.URLField()
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
    
    
    
    
    
    def __str__(self):
        return f'{self.profile.user.username} Image'