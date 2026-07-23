from django.db import models
from jobseeker.models import Jobseeker
from jobs.models import Job

class Application(models.Model):
  user = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  message = models.TextField()
  resume = models.FileField(upload_to='CV', max_length=100)
  create_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.full_name
