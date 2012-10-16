# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.text_rst'
        db.add_column('blog_post', 'text_rst',
                      self.gf('django.db.models.fields.TextField')(default=u''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.text_rst'
        db.delete_column('blog_post', 'text_rst')


    models = {
        'blog.post': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Post'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'edited_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'text_rst': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']