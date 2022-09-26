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