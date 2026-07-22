from django.urls import path
from .views import *

urlpatterns = [
  path('', home, name='home'),
  path('register/', RegisterCreateView.as_view(), name='register'),
  path('login/', SignLoginView.as_view(), name='login'),
  path('logout/', exit, name='logout'),
]