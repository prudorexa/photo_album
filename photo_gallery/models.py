
from django.contrib.auth.models import User
from django.db import models


# Create user and save to the database


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)

    def __str__(self) -> str:
        return self.title
