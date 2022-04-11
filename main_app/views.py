from django.shortcuts import render
from django.views.generic import ListView
from .models import Channel
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Channel :
  def __init__(self, title, description):
    self.title = title
    self.description = description

