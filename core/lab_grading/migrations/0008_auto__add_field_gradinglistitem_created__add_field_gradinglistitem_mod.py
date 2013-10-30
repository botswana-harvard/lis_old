# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GradingListItem.created'
        db.add_column('lab_grading_gradinglistitem', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'GradingListItem.modified'
        db.add_column('lab_grading_gradinglistitem', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'GradingListItem.user_created'
        db.add_column('lab_grading_gradinglistitem', 'user_created',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'GradingListItem.user_modified'
        db.add_column('lab_grading_gradinglistitem', 'user_modified',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'GradingListItem.hostname_created'
        db.add_column('lab_grading_gradinglistitem', 'hostname_created',
                      self.gf('django.db.models.fields.CharField')(default='silverapple', max_length=50, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'GradingListItem.hostname_modified'
        db.add_column('lab_grading_gradinglistitem', 'hostname_modified',
                      self.gf('django.db.models.fields.CharField')(default='silverapple', max_length=50, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'GradingList.created'
        db.add_column('lab_grading_gradinglist', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'GradingList.modified'
        db.add_column('lab_grading_gradinglist', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'GradingList.user_created'
        db.add_column('lab_grading_gradinglist', 'user_created',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'GradingList.user_modified'
        db.add_column('lab_grading_gradinglist', 'user_modified',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'GradingList.hostname_created'
        db.add_column('lab_grading_gradinglist', 'hostname_created',
                      self.gf('django.db.models.fields.CharField')(default='silverapple', max_length=50, db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'GradingList.hostname_modified'
        db.add_column('lab_grading_gradinglist', 'hostname_modified',
                      self.gf('django.db.models.fields.CharField')(default='silverapple', max_length=50, db_index=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GradingListItem.created'
        db.delete_column('lab_grading_gradinglistitem', 'created')

        # Deleting field 'GradingListItem.modified'
        db.delete_column('lab_grading_gradinglistitem', 'modified')

        # Deleting field 'GradingListItem.user_created'
        db.delete_column('lab_grading_gradinglistitem', 'user_created')

        # Deleting field 'GradingListItem.user_modified'
        db.delete_column('lab_grading_gradinglistitem', 'user_modified')

        # Deleting field 'GradingListItem.hostname_created'
        db.delete_column('lab_grading_gradinglistitem', 'hostname_created')

        # Deleting field 'GradingListItem.hostname_modified'
        db.delete_column('lab_grading_gradinglistitem', 'hostname_modified')

        # Deleting field 'GradingList.created'
        db.delete_column('lab_grading_gradinglist', 'created')

        # Deleting field 'GradingList.modified'
        db.delete_column('lab_grading_gradinglist', 'modified')

        # Deleting field 'GradingList.user_created'
        db.delete_column('lab_grading_gradinglist', 'user_created')

        # Deleting field 'GradingList.user_modified'
        db.delete_column('lab_grading_gradinglist', 'user_modified')

        # Deleting field 'GradingList.hostname_created'
        db.delete_column('lab_grading_gradinglist', 'hostname_created')

        # Deleting field 'GradingList.hostname_modified'
        db.delete_column('lab_grading_gradinglist', 'hostname_modified')


    models = {
        'lab_grading.gradinglist': {
            'Meta': {'ordering': "['name']", 'object_name': 'GradingList'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_grading.gradinglistitem': {
            'Meta': {'ordering': "['test_code', 'age_low', 'age_low_unit']", 'object_name': 'GradingListItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'age_high': ('django.db.models.fields.IntegerField', [], {'default': '99999', 'null': 'True', 'blank': 'True'}),
            'age_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10', 'blank': 'True'}),
            'age_high_unit': ('django.db.models.fields.CharField', [], {'default': "'Y'", 'max_length': '10', 'blank': 'True'}),
            'age_low': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'age_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10', 'blank': 'True'}),
            'age_low_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'grading_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_grading.GradingList']"}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'default': "'ANY'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'panic_value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'panic_value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'default': "'increasing'", 'max_length': '25'}),
            'test_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCode']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10'}),
            'value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10'}),
            'value_unit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        'lab_test_code.testcode': {
            'Meta': {'ordering': "['name']", 'object_name': 'TestCode', 'db_table': "'bhp_lab_test_code_testcode'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'formula': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_absolute': ('django.db.models.fields.CharField', [], {'default': "'absolute'", 'max_length': "'15'"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'test_code_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCodeGroup']"}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_test_code.testcodegroup': {
            'Meta': {'ordering': "['code']", 'object_name': 'TestCodeGroup', 'db_table': "'bhp_lab_test_code_testcodegroup'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['lab_grading']