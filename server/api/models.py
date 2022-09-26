from django.db import models
from PIL import Image

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    bio = models.CharField(max_length=500, null=True)
    profile_picture = models.ImageField(null=True)
    experience_level = models.CharField(max_length=30, null=True)
    is_coach = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    certifications = models.CharField(max_length=500, null=True)
    coaching_experience = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.user.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)
    caption = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.caption