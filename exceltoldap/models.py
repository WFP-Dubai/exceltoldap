#LDAP Interface
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    uploaded = models.DateTimeField(auto_now_add=True)
    imported = models.DateTimeField(blank=True, null=True)


class EpicDevice( models.Model):
    deviceUid = models.CharField(max_length = 50, primary_key=True)
    Description = models.CharField(blank=True, null=True, max_length = 200)
    Capabilities = models.CharField(blank=True, null=True, max_length = 20)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EpicUser( models.Model):
    username = models.CharField(primary_key=True, max_length = 50)
    personalTitle = models.CharField(blank=True, null=True, max_length = 50)
    firstName = models.CharField(blank=True, null=True, max_length = 50)
    lastName = models.CharField(blank=True, null=True, max_length = 50)
    eMail = models.CharField(blank=True, null=True, max_length = 100)
    additionalEmails = models.CharField(blank=True, null=True, max_length = 200)
    phoneNumbers = models.CharField(blank=True, null=True, max_length = 200)
    messaging = models.CharField(blank=True, null=True, max_length = 200)
    organization = models.CharField(blank=True, null=True, max_length = 50)
    department = models.CharField(blank=True, null=True, max_length = 50)
    street = models.CharField(blank=True, null=True, max_length = 50)
    zip = models.CharField(blank=True, null=True, max_length = 50)
    city = models.CharField(blank=True, null=True, max_length = 50)
    country = models.CharField(blank=True, null=True, max_length = 50)
    jobTitle = models.CharField(blank=True, null=True, max_length = 50)
    preferredLanguage = models.CharField(blank=True, null=True, max_length = 50)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EpicVehicle( models.Model):
    vehicleID = models.CharField(primary_key=True,max_length = 50)
    description = models.CharField(blank=True, null=True, max_length = 200)
    type = models.CharField(blank=True, null=True, max_length = 20)
    messaging = models.CharField(blank=True, null=True, max_length = 200)
    licensePlate = models.CharField(blank=True, null=True, max_length = 50)
    VIN = models.CharField(blank=True, null=True, max_length = 50)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EpicPlace( models.Model):
    placeID = models.CharField(primary_key=True,max_length = 50)
    compasID = models.CharField(blank=True, null=True, max_length = 50)
    description = models.CharField(blank=True, null=True, max_length = 200)
    type = models.CharField(blank=True, null=True, max_length = 20)
    organization = models.CharField(blank=True, null=True, max_length = 50)
    department = models.CharField(blank=True, null=True, max_length = 20)
    street = models.CharField(blank=True, null=True, max_length = 200)
    zip = models.CharField(blank=True, null=True, max_length = 20)
    city = models.CharField(blank=True, null=True, max_length = 20)
    country = models.CharField(blank=True, null=True, max_length = 20)
    eMail = models.CharField(blank=True, null=True, max_length = 200)
    phoneNumbers = models.CharField(blank=True, null=True, max_length = 200)
    messaging = models.CharField(blank=True, null=True, max_length = 200)
    altitude = models.FloatField( null = True, db_column = 'Altitude', blank = True)
    latitude = models.FloatField( db_column = 'Latitude' , blank = True)
    longitude = models.FloatField( db_column = 'Longitude', blank = True)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)