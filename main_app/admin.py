from django.contrib import admin
from .models import Channel, Profile, Thread, Photo


# Register your models here.
admin.site.register(Channel)
admin.site.register(Profile)
admin.site.register(Thread)
admin.site.register(Photo)