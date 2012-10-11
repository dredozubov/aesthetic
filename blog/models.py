from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=128)
    text = models.TextField()

    def __unicode__(self):
        return '%s, %s' % (self.title, self.created_at)

    class Meta:
        ordering = ['-created_at']
