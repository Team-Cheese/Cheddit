from django.forms import ModelForm
from .models import Thread, UserProfile

class ThreadForm(ModelForm):
  class Meta:
    model = Thread
    fields = ['title', 'body']

class UserProfileForm(ModelForm):
  class Meta:
    model = UserProfile
    fields = ['screen_name']

