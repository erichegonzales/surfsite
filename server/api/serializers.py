from rest_framework import serializers
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        
        fields = '__all__'
        
class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Coach
        fields = '__all__'
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'url', 'image', 'video', 'title', 'content', 'location', 'likes', 'user']
        
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        
class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'
        
class BookedLessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BookedLesson
        fields = '__all__'
        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        
        
class Post_Serializer(serializers.BaseSerializer):
  def to_representation(self,instance):
    return {
      "id":instance.id,
    "image":instance.image,
    "video":instance.video,
    "title":instance.title,
    "content":instance.content,
    "location":instance.location,
    "likes":instance.likes,
    "user":{
        "id": instance.user.id,
        "name": instance.user.name,
        "username": instance.user.username,
        "email": instance.user.email,
        "bio": instance.user.bio,
    }
   
    }