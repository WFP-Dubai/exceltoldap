#LDAP Interface
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class EpicDevice( models.Model):
    deviceUid = models.CharField(max_length = 20, primary_key=True)
    Description = models.CharField(blank=True, null=True, max_length = 20)
    Capabilities = models.CharField(blank=True, null=True, max_length = 20)


class EpicUser( models.Model):
    username = models.CharField(primary_key=True, max_length = 20)
    personalTitle = models.CharField(blank=True, null=True, max_length = 20)
    firstName = models.CharField(blank=True, null=True, max_length = 20)
    lastName = models.CharField(blank=True, null=True, max_length = 20)
    eMail = models.CharField(blank=True, null=True, max_length = 20)
    additionalEmails = models.CharField(blank=True, null=True, max_length = 20)
    phoneNumbers = models.CharField(blank=True, null=True, max_length = 20)
    messaging = models.CharField(blank=True, null=True, max_length = 20)
    organization = models.CharField(blank=True, null=True, max_length = 20)
    department = models.CharField(blank=True, null=True, max_length = 20)
    street = models.CharField(blank=True, null=True, max_length = 20)
    zip = models.CharField(blank=True, null=True, max_length = 20)
    city = models.CharField(blank=True, null=True, max_length = 20)
    country = models.CharField(blank=True, null=True, max_length = 20)
    jobTitle = models.CharField(blank=True, null=True, max_length = 20)
    preferredLanguage = models.CharField(blank=True, null=True, max_length = 20)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)


class EpicVehicle( models.Model):
    vehicleID = models.CharField(primary_key=True,max_length = 20)
    description = models.CharField(blank=True, null=True, max_length = 20)
    type = models.CharField(blank=True, null=True, max_length = 20)
    messaging = models.CharField(blank=True, null=True, max_length = 20)
    licensePlate = models.CharField(blank=True, null=True, max_length = 20)
    VIN = models.CharField(blank=True, null=True, max_length = 20)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)


class EpicPlace( models.Model):
    placeID = models.CharField(primary_key=True,max_length = 20)
    compasID = models.CharField(blank=True, null=True, max_length = 20)
    description = models.CharField(blank=True, null=True, max_length = 20)
    type = models.CharField(blank=True, null=True, max_length = 20)
    organization = models.CharField(blank=True, null=True, max_length = 20)
    department = models.CharField(blank=True, null=True, max_length = 20)
    street = models.CharField(blank=True, null=True, max_length = 20)
    zip = models.CharField(blank=True, null=True, max_length = 20)
    city = models.CharField(blank=True, null=True, max_length = 20)
    country = models.CharField(blank=True, null=True, max_length = 20)
    eMail = models.CharField(blank=True, null=True, max_length = 20)
    phoneNumbers = models.CharField(blank=True, null=True, max_length = 20)
    messaging = models.CharField(blank=True, null=True, max_length = 20)
    altitude = models.FloatField( null = True, db_column = 'Altitude', blank = True)
    latitude = models.FloatField( db_column = 'Latitude' , blank = True)
    longitude = models.FloatField( db_column = 'Longitude', blank = True)
    deviceID = models.ForeignKey(EpicDevice,blank=True, null=True)