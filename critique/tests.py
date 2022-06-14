
from django.test import TestCase
from  .models  import *
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(pro_picture ='image.jpg', bio = 'text', email = 'johndoe@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    def test_save_method(self):
        self.profile.save()    
        