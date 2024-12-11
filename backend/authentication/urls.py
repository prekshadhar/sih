from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('auth/signup/', views.signup, name='auth-signup'),
    path('auth/login/', views.login, name='auth-login'),
]