from django.contrib import admin
from .models import Profile, Ratings, Reviews, Project

# Register your models here.

admin.site.register(Profile)
admin.site.register(Ratings)
admin.site.register(Reviews)
admin.site.register(Project)

