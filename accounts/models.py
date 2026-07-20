from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  JOOB_CHOOISE = [
    ('jobseeker',  'jobseeker'),
    ('employer', 'employer')
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  resume = models.FileField(upload_to='resumes/')
  bio = models.TextField()
  avatar = models.ImageField(upload_to='avatars/')
  role = models.CharField(max_length=50, choices=JOOB_CHOOISE)

  def __str__(self):
    return self.user
