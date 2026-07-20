from django.urls import path
from .views import *

urlpatterns = [
  path('', RegisterCreateView.as_view(), name='register'),
]