from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('channels/', views.channels_index, name='channels_index'),
  path('channels/create/', views.ChannelCreate.as_view(), name='channels_create'),
  path('channels/<str:channel_id>/create_thread/', views.thread_create, name='thread_create'),
  path('channels/<str:channel_id>/', views.channels_details, name='channels_details'),
  # path('accounts/signup', views.signup, name='signup'),
]