from django.contrib import admin
from .models import Category, Job

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
  list_display = ['title']