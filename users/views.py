import requests
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'GET':
        return Response(headers={'Location': 'http://login.typecraft.org?return_to=http://valex.typecraft.org'},
                        status=status.HTTP_302_FOUND)

    username = request.data.get('username')
    password = request.data.get('password')

    response = requests.post('http://login.typecraft.org/login', data={
        'username': username, 'password': password
    })

    # Response expected to contain user information. If the user does not exist in the local database yet,
    # create it. If it doesn't exist remotely, redirect to signup with data
    if response.status_code == 200:
        response_data = response.json()  # Expected to contain a DRF-serialized version of a user
        username = response_data.get('username')
        user = User.objects.filter(username=username).first()

        if not user:
            serializer = UserSerializer(data=response_data, context={'request': request})
            if not serializer.is_valid():
                return Response({
                    'detail': 'Critical error, login server returned bad data.',
                    'source': response_data
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            new_user = serializer.save()
            login(request, new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            login(request, user)
            return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_200_OK)
