# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TestCodeReferenceListItemAudit.hostname_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'hostname_created')

        # Deleting field 'TestCodeReferenceListItemAudit.hostname_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'hostname_modified')

        # Deleting field 'TestCodeReferenceListItemAudit.created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'created')

        # Deleting field 'TestCodeReferenceListItemAudit.user_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'user_modified')

        # Deleting field 'TestCodeReferenceListItemAudit.modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'modified')

        # Deleting field 'TestCodeReferenceListItemAudit.user_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'user_created')


        # Changing field 'TestCodeReferenceListItemAudit._audit_id'
        db.alter_column('bhp_lab_test_code_testcodereferencelistitem_audit', '_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'TestCodeReferenceListItem.hostname_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'hostname_created')

        # Deleting field 'TestCodeReferenceListItem.hostname_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'hostname_modified')

        # Deleting field 'TestCodeReferenceListItem.user_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'user_created')

        # Deleting field 'TestCodeReferenceListItem.user_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'user_modified')

        # Deleting field 'TestCodeReferenceListItem.created'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'created')

        # Deleting field 'TestCodeReferenceListItem.modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelistitem', 'modified')

        # Deleting field 'TestCodeReferenceList.hostname_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'hostname_created')

        # Deleting field 'TestCodeReferenceList.hostname_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'hostname_modified')

        # Deleting field 'TestCodeReferenceList.user_created'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'user_created')

        # Deleting field 'TestCodeReferenceList.created'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'created')

        # Deleting field 'TestCodeReferenceList.user_modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'user_modified')

        # Deleting field 'TestCodeReferenceList.modified'
        db.delete_column('bhp_lab_test_code_testcodereferencelist', 'modified')


    def backwards(self, orm):
        # Adding field 'TestCodeReferenceListItemAudit.hostname_created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'hostname_created',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItemAudit.hostname_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'hostname_modified',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItemAudit.created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItemAudit.user_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'user_modified',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItemAudit.modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItemAudit.user_created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem_audit', 'user_created',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)


        # Changing field 'TestCodeReferenceListItemAudit._audit_id'
        db.alter_column('bhp_lab_test_code_testcodereferencelistitem_audit', '_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True))
        # Adding field 'TestCodeReferenceListItem.hostname_created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'hostname_created',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItem.hostname_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'hostname_modified',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItem.user_created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'user_created',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItem.user_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'user_modified',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItem.created'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceListItem.modified'
        db.add_column('bhp_lab_test_code_testcodereferencelistitem', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.hostname_created'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'hostname_created',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.hostname_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'hostname_modified',
                      self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.user_created'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'user_created',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.created'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.user_modified'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'user_modified',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True),
                      keep_default=False)

        # Adding field 'TestCodeReferenceList.modified'
        db.add_column('bhp_lab_test_code_testcodereferencelist', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    models = {
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
        },
        'lab_test_code.testcodeinterfacemapping': {
            'Meta': {'object_name': 'TestCodeInterfaceMapping', 'db_table': "'bhp_lab_test_code_testcodeinterfacemapping'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'foreign_test_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_test_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCode']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_test_code.testcodereferencelist': {
            'Meta': {'ordering': "['name']", 'object_name': 'TestCodeReferenceList', 'db_table': "'bhp_lab_test_code_testcodereferencelist'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'lab_test_code.testcodereferencelistitem': {
            'Meta': {'ordering': "['test_code', 'age_low', 'age_low_unit']", 'object_name': 'TestCodeReferenceListItem', 'db_table': "'bhp_lab_test_code_testcodereferencelistitem'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'age_high': ('django.db.models.fields.IntegerField', [], {'default': '99999', 'null': 'True', 'blank': 'True'}),
            'age_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10', 'blank': 'True'}),
            'age_high_unit': ('django.db.models.fields.CharField', [], {'default': "'Y'", 'max_length': '10', 'blank': 'True'}),
            'age_low': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'age_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10', 'blank': 'True'}),
            'age_low_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'default': "'ANY'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'panic_value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'panic_value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'default': "'increasing'", 'max_length': '25'}),
            'test_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCode']"}),
            'test_code_reference_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCodeReferenceList']"}),
            'value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10'}),
            'value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10'}),
            'value_unit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        'lab_test_code.testcodereferencelistitemaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'TestCodeReferenceListItemAudit', 'db_table': "'bhp_lab_test_code_testcodereferencelistitem_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'age_high': ('django.db.models.fields.IntegerField', [], {'default': '99999', 'null': 'True', 'blank': 'True'}),
            'age_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10', 'blank': 'True'}),
            'age_high_unit': ('django.db.models.fields.CharField', [], {'default': "'Y'", 'max_length': '10', 'blank': 'True'}),
            'age_low': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'age_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10', 'blank': 'True'}),
            'age_low_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'default': "'ANY'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'panic_value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'panic_value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'default': "'increasing'", 'max_length': '25'}),
            'test_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_testcodereferencelistitem'", 'to': "orm['lab_test_code.TestCode']"}),
            'test_code_reference_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_testcodereferencelistitem'", 'to': "orm['lab_test_code.TestCodeReferenceList']"}),
            'value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10'}),
            'value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10'}),
            'value_unit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['lab_test_code']