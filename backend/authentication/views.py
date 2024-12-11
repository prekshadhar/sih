from django.contrib.auth.models import User  

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Add this new view
@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to the API',
        'endpoints': {
            'signup': '/api/auth/signup/',
            'login': '/api/auth/login/',
            # 'ml_predict': '/api/ml/predict/'
        }
    })

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response({
                "message": "User created successfully",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({
                "message": "Username or email already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email_or_username = request.data.get('email')
    password = request.data.get('password')
    
    if not email_or_username or not password:
        return Response({
            "message": "Both email/username and password are required"
        }, status=status.HTTP_400_BAD_REQUEST)

    # Check if the input is an email or username
    try:
        validate_email(email_or_username)
        # It's an email
        try:
            user = User.objects.get(email=email_or_username)
        except User.DoesNotExist:
            return Response({
                "message": "No user found with this email"
            }, status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        # It's a username
        user = None
    
    if not user:
        user = authenticate(username=email_or_username, password=password)
    else:
        user = authenticate(username=user.username, password=password)
    
    if user:
        return Response({
            "message": "Login successful",
            "user": {
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_200_OK)
    return Response({
        "message": "Invalid credentials"
    }, status=status.HTTP_401_UNAUTHORIZED)