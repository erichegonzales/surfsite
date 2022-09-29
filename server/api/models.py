from django.db import models
from PIL import Image

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True)
    bio = models.CharField(max_length=500, null=True)
    profile_picture = models.ImageField(null=True)
    followers = models.IntegerField(default=0, null=True)
    following = models.IntegerField(default=0, null=True)
    experience_level = models.CharField(max_length=30, null=True)
    is_coach = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Coach(models.Model):
    certifications = models.CharField(max_length=500, null=True)
    coaching_experience = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.name

class Post(models.Model):
    image = models.CharField(max_length=500, null=True)
    video = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=100, null=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.caption
    
class Comment(models.Model):
    content = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.content
    
class Lesson(models.Model):
    title = models.CharField(max_length=50, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(null=True)
    location = models.CharField(max_length=100, null=True)
    avg_rating = models.IntegerField(default=0)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
class BookedLesson(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.lesson.title
    
class Review(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1000, null=True)
    rating = models.IntegerField(default=0)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title