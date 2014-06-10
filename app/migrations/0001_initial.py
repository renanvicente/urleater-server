# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Url'
        db.create_table(u'app_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('urls', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Url'])


    def backwards(self, orm):
        # Deleting model 'Url'
        db.delete_table(u'app_url')


    models = {
        u'app.url': {
            'Meta': {'ordering': "['-title']", 'object_name': 'Url'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'urls': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['app']