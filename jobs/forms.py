from django import forms
from .models import Category, Job

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name', 'description']

class JobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'content', 'field', 'city', 'salary', 'email', 'phone', 'work']
