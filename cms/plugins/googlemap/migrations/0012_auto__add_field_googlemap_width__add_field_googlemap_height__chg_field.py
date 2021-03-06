# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GoogleMap.width'
        db.add_column('cmsplugin_googlemap', 'width',
                      self.gf('django.db.models.fields.CharField')(default='100%', max_length=6),
                      keep_default=False)

        # Adding field 'GoogleMap.height'
        db.add_column('cmsplugin_googlemap', 'height',
                      self.gf('django.db.models.fields.CharField')(default='400px', max_length=6),
                      keep_default=False)

        # Changing field 'GoogleMap.zoom'
        db.alter_column('cmsplugin_googlemap', 'zoom', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=13))

    def backwards(self, orm):
        # Deleting field 'GoogleMap.width'
        db.delete_column('cmsplugin_googlemap', 'width')

        # Deleting field 'GoogleMap.height'
        db.delete_column('cmsplugin_googlemap', 'height')


        # Changing field 'GoogleMap.zoom'
        db.alter_column('cmsplugin_googlemap', 'zoom', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'googlemap.googlemap': {
            'Meta': {'object_name': 'GoogleMap', 'db_table': "'cmsplugin_googlemap'", '_ormbases': ['cms.CMSPlugin']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'400px'", 'max_length': '6'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'route_planer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'route_planer_title': ('django.db.models.fields.CharField', [], {'default': "u'Calculate your fastest way to here'", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '6'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'zoom': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '13'})
        }
    }

    complete_apps = ['googlemap']
