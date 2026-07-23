from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import  reverse_lazy

def home(request):
  return render(request, 'accounts/home.html')

class RegisterCreateView(CreateView):
  form_class = RegisterForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/register.html'

class SignLoginView(LoginView):
  template_name = 'accounts/login.html'

def get_success_url(self):
    user = self.request.user
    if user.is_authenticated and hasattr(user, 'profile'):
        if user.profile.role == 'jobseeker':
            return reverse_lazy('employer')
        elif user.profile.role == 'employer':
            return reverse_lazy('employer')

    return reverse_lazy('home')

def exit(request):
  logout(request)
  return redirect('login')
