from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.authtoken.models import Token
    
User = get_user_model()

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to the API',
        'endpoints': {
            'signup': '/api/auth/signup/',
            'login': '/api/auth/login/',
        }
    })

import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def signup(request):
    logger.info(f"Received signup request: {request.data}")
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user = serializer.save()
            logger.info(f"User created successfully: {user.username}")
            return Response({
                "message": "User created successfully",
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            logger.error(f"IntegrityError during signup: {str(e)}")
            return Response({
                "message": "Username or email already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error during signup: {str(e)}")
            return Response({
                "message": "An unexpected error occurred"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    logger.error(f"Invalid serializer data: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email_or_username = request.data.get('email')
    password = request.data.get('password')
    
    if not email_or_username or not password:
        return Response({
            "message": "Both email/username and password are required"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_email(email_or_username)
        user = User.objects.filter(email=email_or_username).first()
    except ValidationError:
        user = User.objects.filter(username=email_or_username).first()
    
    if user and user.check_password(password):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successful",
            "user": {
                "username": user.username,
                "email": user.email
            },
            "token": token.key
        }, status=status.HTTP_200_OK)
    return Response({
        "message": "Invalid credentials"
    }, status=status.HTTP_401_UNAUTHORIZED)