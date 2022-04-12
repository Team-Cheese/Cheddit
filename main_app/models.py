from django.db import models
from django.contrib.auth.models import User
import uuid 
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Channel(models.Model):
  title = models.CharField('Channel Title', max_length=100, unique=True)
  # created_by = models.ForeignKey(Profile)
  description = models.TextField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('channels_details', kwargs={'channel_id' : self.id})

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  screen_name=models.TextField(max_length=15, unique=True)

  def __str__(self):
    return f'{self.screen_name} Profile'

class Thread(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  # created_by = models.ForeignKey(Profile)
  title = models.CharField('Thread Title',max_length=100, unique=True)
  created = models.DateTimeField(auto_now_add=True)
  body = RichTextField(blank=True, null=True)
  channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)

  

class Photo(models.Model):
  url = models.CharField(max_length=250)
  thread = models.OneToOneField(Thread, on_delete=models.CASCADE)

  def __str__(self):
    return f'Photo for thread {self.thread_id}'

