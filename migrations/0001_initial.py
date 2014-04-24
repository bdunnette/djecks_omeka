# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repository'
        db.create_table(u'djecks_omeka_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'djecks_omeka', ['Repository'])

        # Adding model 'Collection'
        db.create_table(u'djecks_omeka_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('items_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks_omeka.Repository'])),
            ('deck', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Deck'], null=True, blank=True)),
        ))
        db.send_create_signal(u'djecks_omeka', ['Collection'])

        # Adding model 'Item'
        db.create_table(u'djecks_omeka_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('files_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks_omeka.Collection'])),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks.Case'], null=True, blank=True)),
        ))
        db.send_create_signal(u'djecks_omeka', ['Item'])

        # Adding model 'Image'
        db.create_table(u'djecks_omeka_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_annotated', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djecks_omeka.Item'])),
        ))
        db.send_create_signal(u'djecks_omeka', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Repository'
        db.delete_table(u'djecks_omeka_repository')

        # Deleting model 'Collection'
        db.delete_table(u'djecks_omeka_collection')

        # Deleting model 'Item'
        db.delete_table(u'djecks_omeka_item')

        # Deleting model 'Image'
        db.delete_table(u'djecks_omeka_image')


    models = {
        u'djecks.case': {
            'Meta': {'object_name': 'Case'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'decks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks.deck': {
            'Meta': {'object_name': 'Deck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks_omeka.collection': {
            'Meta': {'object_name': 'Collection'},
            'deck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks_omeka.Repository']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'djecks_omeka.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_annotated': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks_omeka.Item']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks_omeka.item': {
            'Meta': {'object_name': 'Item'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks.Case']", 'null': 'True', 'blank': 'True'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djecks_omeka.Collection']"}),
            'files_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'djecks_omeka.repository': {
            'Meta': {'object_name': 'Repository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['djecks_omeka']