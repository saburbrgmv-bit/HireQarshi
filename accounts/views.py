from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.auth import logout

def home(request):
    return render(request, 'accounts/home.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class LoginUserView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.profile.role == 'jobseeker':
            return reverse_lazy('employers')
        elif user.profile.role == 'employer':
            return reverse_lazy('employers')
        return reverse_lazy('home')


def exit(request):
    logout(request)
    return redirect('login')