# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URLAssociation'
        db.create_table('shortener_urlassociation', (
            ('short_url', self.gf('django.db.models.fields.CharField')(max_length=64, primary_key=True)),
            ('actual_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('shortener', ['URLAssociation'])

    def backwards(self, orm):
        # Deleting model 'URLAssociation'
        db.delete_table('shortener_urlassociation')

    models = {
        'shortener.urlassociation': {
            'Meta': {'object_name': 'URLAssociation'},
            'actual_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.CharField', [], {'max_length': '64', 'primary_key': 'True'})
        }
    }

    complete_apps = ['shortener']