from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DataTimeField(auto_now=True)
    text = models.TextField()
