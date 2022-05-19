from django.db import models
from django.contrib.auth.models import User


class UsersAdditionalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField()


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
