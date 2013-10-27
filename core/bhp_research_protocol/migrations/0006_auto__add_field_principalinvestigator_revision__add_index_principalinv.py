# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PrincipalInvestigator.revision'
        db.add_column(u'bhp_research_protocol_principalinvestigator', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding index on 'PrincipalInvestigator', fields ['hostname_created']
        db.create_index(u'bhp_research_protocol_principalinvestigator', ['hostname_created'])

        # Adding index on 'PrincipalInvestigator', fields ['user_modified']
        db.create_index(u'bhp_research_protocol_principalinvestigator', ['user_modified'])

        # Adding index on 'PrincipalInvestigator', fields ['hostname_modified']
        db.create_index(u'bhp_research_protocol_principalinvestigator', ['hostname_modified'])

        # Adding index on 'PrincipalInvestigator', fields ['user_created']
        db.create_index(u'bhp_research_protocol_principalinvestigator', ['user_created'])

        # Adding field 'SiteLeader.revision'
        db.add_column(u'bhp_research_protocol_siteleader', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding index on 'SiteLeader', fields ['hostname_created']
        db.create_index(u'bhp_research_protocol_siteleader', ['hostname_created'])

        # Adding index on 'SiteLeader', fields ['user_modified']
        db.create_index(u'bhp_research_protocol_siteleader', ['user_modified'])

        # Adding index on 'SiteLeader', fields ['hostname_modified']
        db.create_index(u'bhp_research_protocol_siteleader', ['hostname_modified'])

        # Adding index on 'SiteLeader', fields ['user_created']
        db.create_index(u'bhp_research_protocol_siteleader', ['user_created'])


    def backwards(self, orm):
        # Removing index on 'SiteLeader', fields ['user_created']
        db.delete_index(u'bhp_research_protocol_siteleader', ['user_created'])

        # Removing index on 'SiteLeader', fields ['hostname_modified']
        db.delete_index(u'bhp_research_protocol_siteleader', ['hostname_modified'])

        # Removing index on 'SiteLeader', fields ['user_modified']
        db.delete_index(u'bhp_research_protocol_siteleader', ['user_modified'])

        # Removing index on 'SiteLeader', fields ['hostname_created']
        db.delete_index(u'bhp_research_protocol_siteleader', ['hostname_created'])

        # Removing index on 'PrincipalInvestigator', fields ['user_created']
        db.delete_index(u'bhp_research_protocol_principalinvestigator', ['user_created'])

        # Removing index on 'PrincipalInvestigator', fields ['hostname_modified']
        db.delete_index(u'bhp_research_protocol_principalinvestigator', ['hostname_modified'])

        # Removing index on 'PrincipalInvestigator', fields ['user_modified']
        db.delete_index(u'bhp_research_protocol_principalinvestigator', ['user_modified'])

        # Removing index on 'PrincipalInvestigator', fields ['hostname_created']
        db.delete_index(u'bhp_research_protocol_principalinvestigator', ['hostname_created'])

        # Deleting field 'PrincipalInvestigator.revision'
        db.delete_column(u'bhp_research_protocol_principalinvestigator', 'revision')

        # Deleting field 'SiteLeader.revision'
        db.delete_column(u'bhp_research_protocol_siteleader', 'revision')


    models = {
        'bhp_research_protocol.funder': {
            'Meta': {'ordering': "['name']", 'object_name': 'Funder'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bhp_research_protocol.fundingsource': {
            'Meta': {'ordering': "['name']", 'object_name': 'FundingSource'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        'bhp_research_protocol.location': {
            'Meta': {'ordering': "['name']", 'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        'bhp_research_protocol.principalinvestigator': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'unique_together': "(['last_name', 'first_name'],)", 'object_name': 'PrincipalInvestigator'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_research_protocol.protocol': {
            'Meta': {'ordering': "['protocol_identifier']", 'object_name': 'Protocol'},
            'date_opened': ('django.db.models.fields.DateField', [], {}),
            'date_registered': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'funding_source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_research_protocol.FundingSource']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_title': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'protocol_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'research_title': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'site_name_fragment': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'bhp_research_protocol.researchclinic': {
            'Meta': {'ordering': "['name']", 'object_name': 'ResearchClinic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'protocol': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_research_protocol.Protocol']", 'unique': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_research_protocol.Site']"})
        },
        'bhp_research_protocol.site': {
            'Meta': {'ordering': "['site_identifier']", 'object_name': 'Site'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_research_protocol.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'site_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        },
        'bhp_research_protocol.siteleader': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'unique_together': "(['last_name', 'first_name'],)", 'object_name': 'SiteLeader'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_research_protocol.sponsor': {
            'Meta': {'ordering': "['name']", 'object_name': 'Sponsor'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['bhp_research_protocol']