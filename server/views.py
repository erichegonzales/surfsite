# from logging import exception
# from django.http import JsonResponse
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def user_list(request, format=None):
    
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
 