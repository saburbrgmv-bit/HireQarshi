from django.urls import path
from .views import *

urlpatterns = [
  path('create/', ApplicationCreateView.as_view(), name='app_create'),
]