from django.contrib import admin
from .models import Jobseeker

@admin.register(Jobseeker)
class JobseekerAdmin(admin.ModelAdmin):
  list_display = ['full_name']
