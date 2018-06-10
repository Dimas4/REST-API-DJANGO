from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Lang(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title