from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  create_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Job(models.Model):
  JOOB_TYPE = [
    ('Full time', 'Tuliq'),
    ('Part time', 'Qisman'),
    ('Remote', 'Masofaviy'),
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField()
  field = models.ForeignKey(Category, on_delete=models.CASCADE)
  city = models.CharField(max_length=50)
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  email = models.EmailField()
  phone = models.CharField(max_length=50)
  work = models.CharField(max_length=150, choices=JOOB_TYPE)
  create_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


