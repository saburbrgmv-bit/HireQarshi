from django import forms
from .models import Jobseeker

class JobseekerForm(forms.ModelForm):
  class Meta:
    model = Jobseeker
    fields = ['user', 'resume', 'full_name', 'skills', 'phone']
    