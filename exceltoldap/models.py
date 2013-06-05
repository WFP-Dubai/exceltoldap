#LDAP Interface
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='%Y/%m/%d')
    missionName = models.CharField(max_length = 150,blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    imported = models.DateTimeField(blank=True, null=True)



class EpicUser( models.Model):
    username = models.CharField(primary_key=True, max_length = 50)
    personalTitle = models.CharField(blank=True, null=True, max_length = 50)
    firstName = models.CharField(blank=True, null=True, max_length = 50)
    lastName = models.CharField(blank=True, null=True, max_length = 50)
    eMail = models.CharField(blank=True, null=True, max_length = 100)
    #additionalEmails = models.CharField(blank=True, null=True, max_length = 200)
    mobilePhoneNumber = models.CharField(blank=True, null=True, max_length = 200)
    satelitePhoneNumber = models.CharField(blank=True, null=True, max_length = 200)
    officePhoneNumber = models.CharField(blank=True, null=True, max_length = 200)
    wavePhoneNumber = models.CharField(blank=True, null=True, max_length = 200)
    foodsat = models.CharField(max_length=20, blank=True, null=True, help_text="")
    
    #messaging = models.CharField(blank=True, null=True, max_length = 200)
    sip = models.CharField(blank=True, null=True, max_length = 200)
    skype = models.CharField(blank=True, null=True, max_length = 200)
    msnim = models.CharField(blank=True, null=True, max_length = 200)
    vhfCallsign = models.CharField(max_length=10, blank=True, null=True, help_text="")
    
    organization = models.CharField(blank=True, null=True, max_length = 50)
    department = models.CharField(blank=True, null=True, max_length = 50)
    street = models.CharField(blank=True, null=True, max_length = 200)
    zip = models.CharField(blank=True, null=True, max_length = 50)
    city = models.CharField(blank=True, null=True, max_length = 50)
    country = models.CharField(blank=True, null=True, max_length = 50)
    jobTitle = models.CharField(blank=True, null=True, max_length = 50)
    preferredLanguage = models.CharField(blank=True, null=True, max_length = 50)
        
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class EpicVehicle( models.Model):
    vehicleID = models.CharField(primary_key=True,max_length = 50)
    description = models.CharField(blank=True, null=True, max_length = 200)
    type = models.CharField(blank=True, null=True, max_length = 20)
    vhfCallsign = models.CharField(blank=True, null=True, max_length = 200)
    HFCallsign  = models.CharField(blank=True, null=True, max_length = 200)
    licensePlate = models.CharField(blank=True, null=True, max_length = 50)
    VIN = models.CharField(blank=True, null=True, max_length = 50)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organization = models.CharField(blank=True, null=True, max_length = 20)
    department = models.CharField(blank=True, null=True, max_length = 20)



class EpicPlace( models.Model):
    placeID = models.CharField(primary_key=True,max_length = 50)
    compasID = models.CharField(blank=True, null=True, max_length = 50)
    description = models.CharField(blank=True, null=True, max_length = 200)
    type = models.CharField(blank=True, null=True, max_length = 20)
    organization = models.CharField(blank=True, null=True, max_length = 50)
    department = models.CharField(blank=True, null=True, max_length = 20)
    street = models.CharField(blank=True, null=True, max_length = 200)
    zip = models.CharField(blank=True, null=True, max_length = 20)
    city = models.CharField(blank=True, null=True, max_length = 200)
    country = models.CharField(blank=True, null=True, max_length = 20)
    eMail = models.CharField(blank=True, null=True, max_length = 200)
    phoneNumbers = models.CharField(blank=True, null=True, max_length = 200)
    messaging = models.CharField(blank=True, null=True, max_length = 200)
    altitude = models.FloatField( null = True, db_column = 'Altitude', blank = True)
    latitude = models.FloatField( db_column = 'Latitude' ,null=True, blank = True)
    longitude = models.FloatField( db_column = 'Longitude', null=True,blank = True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class EpicDevice( models.Model):
    deviceUid = models.CharField(max_length = 50, primary_key=True)
    description = models.CharField(blank=True, null=True, max_length = 200)
    capabilities = models.CharField(blank=True, null=True, max_length = 20)
    type = models.CharField(blank=True, null=True, max_length = 20)
    owner = models.ForeignKey(EpicUser,blank=True, null=True)
    vehicle = models.ForeignKey(EpicVehicle,blank=True, null=True)
    place = models.ForeignKey(EpicPlace,blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    
    