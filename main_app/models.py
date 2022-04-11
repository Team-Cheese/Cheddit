from django.db import models

# Create your models here.
class Channel(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title