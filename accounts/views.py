from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegisterCreateView(CreateView):
  form_class = RegisterForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/register.html'