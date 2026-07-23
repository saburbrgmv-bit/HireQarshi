from django.urls import path
from .views import *

urlpatterns = [
  path('workers/', JobseekerProfile.as_view(), name="workers"),
]