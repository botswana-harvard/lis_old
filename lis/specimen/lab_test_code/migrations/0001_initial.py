# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestCodeGroup'
        db.create_table('bhp_lab_test_code_testcodegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal('lab_test_code', ['TestCodeGroup'])

        # Adding model 'TestCode'
        db.create_table('bhp_lab_test_code_testcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('display_decimal_places', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_absolute', self.gf('django.db.models.fields.CharField')(default='absolute', max_length='15')),
            ('formula', self.gf('django.db.models.fields.CharField')(max_length='50', null=True, blank=True)),
            ('test_code_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_test_code.TestCodeGroup'])),
        ))
        db.send_create_signal('lab_test_code', ['TestCode'])

        # Adding model 'TestCodeInterfaceMapping'
        db.create_table('bhp_lab_test_code_testcodeinterfacemapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('foreign_test_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('local_test_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_test_code.TestCode'])),
        ))
        db.send_create_signal('lab_test_code', ['TestCodeInterfaceMapping'])

        # Adding model 'TestCodeReferenceList'
        db.create_table('bhp_lab_test_code_testcodereferencelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('list_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('lab_test_code', ['TestCodeReferenceList'])

        # Adding model 'TestCodeReferenceListItemAudit'
        db.create_table('bhp_lab_test_code_testcodereferencelistitem_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('scale', self.gf('django.db.models.fields.CharField')(default='increasing', max_length=25)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hiv_status', self.gf('django.db.models.fields.CharField')(default='ANY', max_length=10)),
            ('value_unit', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('value_low', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('value_low_quantifier', self.gf('django.db.models.fields.CharField')(default='>=', max_length=10)),
            ('value_high', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('value_high_quantifier', self.gf('django.db.models.fields.CharField')(default='<=', max_length=10)),
            ('age_low', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('age_low_unit', self.gf('django.db.models.fields.CharField')(default='D', max_length=10, blank=True)),
            ('age_low_quantifier', self.gf('django.db.models.fields.CharField')(default='>=', max_length=10, blank=True)),
            ('age_high', self.gf('django.db.models.fields.IntegerField')(default=99999, null=True, blank=True)),
            ('age_high_unit', self.gf('django.db.models.fields.CharField')(default='Y', max_length=10, blank=True)),
            ('age_high_quantifier', self.gf('django.db.models.fields.CharField')(default='<=', max_length=10, blank=True)),
            ('panic_value_low', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('panic_value_high', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dummy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('import_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('test_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_testcodereferencelistitem', to=orm['lab_test_code.TestCode'])),
            ('test_code_reference_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_testcodereferencelistitem', to=orm['lab_test_code.TestCodeReferenceList'])),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('lab_test_code', ['TestCodeReferenceListItemAudit'])

        # Adding model 'TestCodeReferenceListItem'
        db.create_table('bhp_lab_test_code_testcodereferencelistitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, db_index=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('scale', self.gf('django.db.models.fields.CharField')(default='increasing', max_length=25)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hiv_status', self.gf('django.db.models.fields.CharField')(default='ANY', max_length=10)),
            ('value_unit', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('value_low', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('value_low_quantifier', self.gf('django.db.models.fields.CharField')(default='>=', max_length=10)),
            ('value_high', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('value_high_quantifier', self.gf('django.db.models.fields.CharField')(default='<=', max_length=10)),
            ('age_low', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('age_low_unit', self.gf('django.db.models.fields.CharField')(default='D', max_length=10, blank=True)),
            ('age_low_quantifier', self.gf('django.db.models.fields.CharField')(default='>=', max_length=10, blank=True)),
            ('age_high', self.gf('django.db.models.fields.IntegerField')(default=99999, null=True, blank=True)),
            ('age_high_unit', self.gf('django.db.models.fields.CharField')(default='Y', max_length=10, blank=True)),
            ('age_high_quantifier', self.gf('django.db.models.fields.CharField')(default='<=', max_length=10, blank=True)),
            ('panic_value_low', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('panic_value_high', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=4, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dummy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('import_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('test_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_test_code.TestCode'])),
            ('test_code_reference_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lab_test_code.TestCodeReferenceList'])),
        ))
        db.send_create_signal('lab_test_code', ['TestCodeReferenceListItem'])


    def backwards(self, orm):
        # Deleting model 'TestCodeGroup'
        db.delete_table('bhp_lab_test_code_testcodegroup')

        # Deleting model 'TestCode'
        db.delete_table('bhp_lab_test_code_testcode')

        # Deleting model 'TestCodeInterfaceMapping'
        db.delete_table('bhp_lab_test_code_testcodeinterfacemapping')

        # Deleting model 'TestCodeReferenceList'
        db.delete_table('bhp_lab_test_code_testcodereferencelist')

        # Deleting model 'TestCodeReferenceListItemAudit'
        db.delete_table('bhp_lab_test_code_testcodereferencelistitem_audit')

        # Deleting model 'TestCodeReferenceListItem'
        db.delete_table('bhp_lab_test_code_testcodereferencelistitem')


    models = {
        'lab_test_code.testcode': {
            'Meta': {'ordering': "['name']", 'object_name': 'TestCode', 'db_table': "'bhp_lab_test_code_testcode'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'formula': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_test_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCode']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'lab_test_code.testcodereferencelist': {
            'Meta': {'ordering': "['name']", 'object_name': 'TestCodeReferenceList', 'db_table': "'bhp_lab_test_code_testcodereferencelist'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'default': "'ANY'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'panic_value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'panic_value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'default': "'increasing'", 'max_length': '25'}),
            'test_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCode']"}),
            'test_code_reference_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lab_test_code.TestCodeReferenceList']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'default': "'ANY'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'import_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'panic_value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'panic_value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'default': "'increasing'", 'max_length': '25'}),
            'test_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_testcodereferencelistitem'", 'to': "orm['lab_test_code.TestCode']"}),
            'test_code_reference_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_testcodereferencelistitem'", 'to': "orm['lab_test_code.TestCodeReferenceList']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'value_high': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_high_quantifier': ('django.db.models.fields.CharField', [], {'default': "'<='", 'max_length': '10'}),
            'value_low': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'value_low_quantifier': ('django.db.models.fields.CharField', [], {'default': "'>='", 'max_length': '10'}),
            'value_unit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['lab_test_code']