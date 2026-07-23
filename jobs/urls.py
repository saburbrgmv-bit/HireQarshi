from django.urls import path
from .views import *

urlpatterns = [
  path('jobs/', JobListView.as_view(), name="employer"),
  path('create/', JobCreateView.as_view(), name="create"),
  path('update/<int:pk>/', JobUpdateView.as_view(), name="update"),
  path('delete/<int:pk>/', JobDeleteView.as_view(), name="delete"),
  path('detail/<int:pk>/', JobDetailView.as_view(), name="detail"),


]