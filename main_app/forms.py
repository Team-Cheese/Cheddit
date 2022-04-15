from django.forms import ModelForm
from .models import Thread, UserProfile, Comment

class ThreadForm( ModelForm ):
  class Meta:
    model = Thread
    fields = [ 'title', 'body' ]

class UserProfileForm( ModelForm ):
  class Meta:
    model = UserProfile
    fields = [ 'screen_name' ]

class CommentForm( ModelForm ):
  class Meta:
    model = Comment
    fields = [ 'body' ]