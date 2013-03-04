# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now=True)
    title = models.CharField(u'Название', max_length=255)
    slug = models.CharField(u'slug(англ)', max_length=128, unique=True)
    text = models.TextField(u'Текст', default=u'')
    text_rst = models.TextField(u'Текст(rst)', default=u'')

    def __unicode__(self):
        return '%s, %s' % (self.title, self.created_at)

    class Meta:
        ordering = ['-created_at']

    def save(self):
        from docutils.core import publish_parts
        parts = publish_parts(
                self.text_rst,
                writer_name='html',
                settings_overrides={'input_encoding': 'unicode'})
        self.text = parts['html_body']
        super(Post, self).save()
