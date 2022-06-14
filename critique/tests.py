
from django.test import TestCase
from  .models  import Profile, Project, Reviews
# Create your tests here.

class ProfileTestClass(TestCase):
    '''profile test class'''
    
    def setUp(self):
        self.profile = Profile(pro_picture ='image.jpg', bio = 'text', email = 'johndoe@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    def test_save_method(self):
        self.profile.save() 
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)   

class ProjectTestClass(TestCase):
    '''project test class'''
       
        
    def setUp(self):
        self.project = Project(image = 'image.jpg', projectname = 'project', description = 'text') 
            
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))  
    
    def tearDown(self):
        Project.objects.all().delete      
    
class ReviewsTestClass(TestCase):
    '''reviews test class'''
    
    def setup(self):
        self.reviews = Reviews(text='text')
        self.reviews.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.reviews,Reviews))       
            
    def tearDown(self):
        Reviews.objects.all().delete
            