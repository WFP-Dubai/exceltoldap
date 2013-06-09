# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'exceltoldap_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('missionName', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('imported', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'exceltoldap', ['Document'])

        # Adding model 'EpicUser'
        db.create_table(u'exceltoldap_epicuser', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('personalTitle', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('eMail', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mobilePhoneNumber', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('satelitePhoneNumber', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('officePhoneNumber', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wavePhoneNumber', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('foodsat', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('sip', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('msnim', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('vhfCallsign', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('jobTitle', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('preferredLanguage', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exceltoldap', ['EpicUser'])

        # Adding model 'EpicVehicle'
        db.create_table(u'exceltoldap_epicvehicle', (
            ('vehicleID', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('vhfCallsign', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('HFCallsign', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('licensePlate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('VIN', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'exceltoldap', ['EpicVehicle'])

        # Adding model 'EpicPlace'
        db.create_table(u'exceltoldap_epicplace', (
            ('placeID', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('compasID', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('eMail', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phoneNumbers', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('messaging', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('altitude', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Altitude', blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Latitude', blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, db_column='Longitude', blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exceltoldap', ['EpicPlace'])

        # Adding model 'EpicDevice'
        db.create_table(u'exceltoldap_epicdevice', (
            ('deviceUid', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('capabilities', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exceltoldap.EpicUser'], null=True, blank=True)),
            ('vehicle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exceltoldap.EpicVehicle'], null=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exceltoldap.EpicPlace'], null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exceltoldap', ['EpicDevice'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'exceltoldap_document')

        # Deleting model 'EpicUser'
        db.delete_table(u'exceltoldap_epicuser')

        # Deleting model 'EpicVehicle'
        db.delete_table(u'exceltoldap_epicvehicle')

        # Deleting model 'EpicPlace'
        db.delete_table(u'exceltoldap_epicplace')

        # Deleting model 'EpicDevice'
        db.delete_table(u'exceltoldap_epicdevice')


    models = {
        u'exceltoldap.document': {
            'Meta': {'object_name': 'Document'},
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'missionName': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'exceltoldap.epicdevice': {
            'Meta': {'ordering': "['deviceUid']", 'object_name': 'EpicDevice'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'capabilities': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'deviceUid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exceltoldap.EpicUser']", 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exceltoldap.EpicPlace']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vehicle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exceltoldap.EpicVehicle']", 'null': 'True', 'blank': 'True'})
        },
        u'exceltoldap.epicplace': {
            'Meta': {'ordering': "['placeID']", 'object_name': 'EpicPlace'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'altitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Altitude'", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'compasID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'eMail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Latitude'", 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'Longitude'", 'blank': 'True'}),
            'messaging': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phoneNumbers': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'placeID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'exceltoldap.epicuser': {
            'Meta': {'ordering': "['username']", 'object_name': 'EpicUser'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'eMail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'foodsat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'jobTitle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mobilePhoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'msnim': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'officePhoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'personalTitle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'preferredLanguage': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'satelitePhoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sip': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'vhfCallsign': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'wavePhoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'exceltoldap.epicvehicle': {
            'HFCallsign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['vehicleID']", 'object_name': 'EpicVehicle'},
            'VIN': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'licensePlate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vehicleID': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'vhfCallsign': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exceltoldap']