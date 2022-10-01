from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    
    
class CoachViewSet(viewsets.ModelViewSet):
    queryset = models.Coach.objects.all()
    serializer_class = serializers.CoachSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    
class BookedLessonViewSet(viewsets.ModelViewSet):
    queryset = models.BookedLesson.objects.all()
    serializer_class = serializers.BookedLessonSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
class Post_ViewSet(APIView):
    def get(self, request):
        try:
            y
            post_results = models.Post.objects.all()
            all_posts = serializers.Post_Serializer(post_results, many=True)
            return Response(all_posts.data)
        except: 
            return Response({'error':"somthing went wrong"})