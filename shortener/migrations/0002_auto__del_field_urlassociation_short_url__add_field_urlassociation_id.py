# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'URLAssociation.short_url'
        db.delete_column('shortener_urlassociation', 'short_url')

        # Adding field 'URLAssociation.id'
        db.add_column('shortener_urlassociation', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'URLAssociation.short_url'
        raise RuntimeError("Cannot reverse this migration. 'URLAssociation.short_url' and its values cannot be restored.")
        # Deleting field 'URLAssociation.id'
        db.delete_column('shortener_urlassociation', 'id')

    models = {
        'shortener.urlassociation': {
            'Meta': {'object_name': 'URLAssociation'},
            'actual_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['shortener']