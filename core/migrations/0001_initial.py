# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'core_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('venue_id', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'core', ['Place'])

        # Adding model 'Consumer'
        db.create_table(u'core_consumer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foursquare_uid', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length='1')),
        ))
        db.send_create_signal(u'core', ['Consumer'])

        # Adding model 'Rating'
        db.create_table(u'core_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consumer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Consumer'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Place'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(default='po', max_length=2)),
            ('median_age', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'core_place')

        # Deleting model 'Consumer'
        db.delete_table(u'core_consumer')

        # Deleting model 'Rating'
        db.delete_table(u'core_rating')


    models = {
        u'core.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'foursquare_uid': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': "'1'"})
        },
        u'core.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venue_id': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'core.rating': {
            'Meta': {'object_name': 'Rating'},
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Consumer']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'median_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Place']"}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'po'", 'max_length': '2'})
        }
    }

    complete_apps = ['core']