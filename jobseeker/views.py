from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Jobseeker
from .forms import JobseekerForm

class JobseekerProfile(ListView):
  model = Jobseeker
  template_name = 'jobseeker/jobseeker_list.html'
  context_object_name = 'jobseekers'