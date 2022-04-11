from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('channels/', views.channels_index, name='channels_index'),
  path('channels/<init:channel_id/', views.channels_detail, name='channels_detail'),
  path('accounts/signup', views.signup, name='signup'),
]