from django.contrib import admin
from .models import Profile, Like, Dislike

# Register your models here.

admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Dislike)
