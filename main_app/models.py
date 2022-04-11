from django.db import models
from django.contrib.auth.models import User
import uuid 

# Create your models here.
class Channel(models.Model):
  title = models.CharField('Channel Title', max_length=100, unique=True)
  # created_by = models.ForeignKey(Profile)
  description = models.TextField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return self.title

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  screen_name=models.TextField(max_length=15, unique=True)

  def __str__(self):
    return f'{self.screen_name} Profile'