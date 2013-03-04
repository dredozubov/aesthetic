# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Post', fields ['slug']
        db.create_unique('blog_post', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['slug']
        db.delete_unique('blog_post', ['slug'])


    models = {
        'blog.post': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Post'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'edited_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'text_rst': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']