from django.db import models
from django.contrib.auth.models import User

class Jobseeker(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  resume = models.FileField(upload_to='resumes', max_length=100)
  full_name = models.CharField(max_length=150)
  skills = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)

  def __str__(self):
    return self.user.username