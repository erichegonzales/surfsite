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
        fields = '__all__'
        
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