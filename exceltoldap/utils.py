from models import EpicUser, EpicPlace, EpicVehicle,EpicDevice
import datetime
import xlrd
import settings


def parse_excel(uploaded_file):
    # read file
    # Check file correct file
    # open Excel
    
    workbook = xlrd.open_workbook(settings.MEDIA_ROOT + uploaded_file.docfile.url)
    get_columns_user()    
    #Call import users
    
    users = workbook.sheet_by_name(u'Users')
    import_users(users)
    places = workbook.sheet_by_name(u'Places')
    import_places(places)
    vehicles = workbook.sheet_by_name(u'Vehicles')
    import_vehicles(vehicles)
    devices = workbook.sheet_by_name(u'Devices')
    import_devices(devices)
    
    # update docfile
    uploaded_file.imported = datetime.datetime.now()
    uploaded_file.save()
    return True

def man_parse_xl(file):
    workbook = xlrd.open_workbook(file)
    
    #Call import users
    users = workbook.sheet_by_name(u'Users')
    import_users(users)
    places = workbook.sheet_by_name(u'Places')
    import_places(places)
    vehicles = workbook.sheet_by_name(u'Vehicles')
    import_vehicles(vehicles)
    
    devices = workbook.sheet_by_name(u'Devices')
    import_devices(devices)
    # update docfile
    uploaded_file.imported = datetime.datetime.now()
    uploaded_file.save()
    return True




def import_users(worksheet):
    num_rows = worksheet.nrows - 1
    curr_row = 1

    users = EpicUser.objects.all()
    for user in users:
        user.delete()
    while curr_row < num_rows:
        curr_row += 1
        #try:
        make_user(worksheet,curr_row)
        #except:
        #    pass
    return True


def import_places(worksheet):
    num_rows = worksheet.nrows - 1
    curr_row = 1
    items = EpicPlace.objects.all()
    for item in items:
        try:
            item.delete()
        except:
            pass
    while curr_row < num_rows:
        curr_row += 1
        make_place(worksheet,curr_row)    
    return True

def import_devices(worksheet):
    num_rows = worksheet.nrows - 1
    curr_row = 1
    items = EpicDevice.objects.all()
    for item in items:
        try:
            item.delete()
        except:
            pass
    while curr_row < num_rows:
        curr_row += 1
        make_device(worksheet,curr_row)    
    return True

def import_vehicles(worksheet):
    num_rows = worksheet.nrows - 1
    curr_row = 1
    items = EpicVehicle.objects.all()
    for item in items:
        item.delete()
    while curr_row < num_rows:
        curr_row += 1
        make_vehicle(worksheet,curr_row)
    return True


def get_columns_user():
    #USERS
    global cusername
    global cpersonal_title
    global cFirstName
    global cLastName
    global ceMail
    global cmobile
    global csatellite
    global coffice
    global cradio
    global cfoodsat
    global csip
    global cskype
    global cmsnim    
    global cVHFcallsign
    global cOrganization
    global cDepartment
    global cStreet
    global cZip
    global cCity
    global cCountry
    global cJobTitle
    global cPreferredLanguage
    ##Cars
    global cVehicleID
    global cVehicleDescription
    global cVehicleType
    global cVehicleVHFcallsign
    global cVehicleHfcallsign
    global cLicensePlate
    global cVIN
    global cMotoTrboID
    global cSatamatics
    global cGVLP
    ##Devices
    global cDeviceUID
    global cDevDescription
    global cDevType
    global cCapabilities
    global cDevUserID
    global cDevVehicleID
    global cDevPlacesID
    cusername    	=   0
    cpersonal_title  =   1
    cFirstName  	    =   2
    cLastName   	    =   3
    ceMail   	    =   4
    cmobile	        =   5
    csatellite	    =   6
    coffice	        =   7
    cradio	        =   8
    cfoodsat	        =   9
    csip	            =   10
    cskype	        =   11
    cmsnim	        =   12
    cVHFcallsign	    =   13
    cOrganization	=   14
    cDepartment	    =   15
    cStreet	        =   16
    cZip	            =   17
    cCity	        =   18
    cCountry	        =   19
    cJobTitle	    =   20
    cPreferredLanguage	=21
    cVehicleID   =   0
    cVehicleDescription =   1
    cVehicleType        =   2
    cVehicleVHFcallsign =   3
    cVehicleHfcallsign  =   4
    cLicensePlate=   5
    cVIN         =   6
    cMotoTrboID  =   7
    cSatamatics  =   8
    cGVLP        =   9
    cDeviceUID   =   0
    cDevDescription =   1
    cDevType        =   2
    cCapabilities=   3
    cDevUserID      =   4
    cDevVehicleID   =   5
    cDevPlacesID    =   6


def make_user(worksheet,curr_row):
    if worksheet.cell_value(curr_row,0) != '':
        item,new = EpicUser.objects.get_or_create(username =  worksheet.cell_value(curr_row,cusername))
        print worksheet.cell_value(curr_row,cpersonal_title)
        item.personalTitle = worksheet.cell_value(curr_row,cpersonal_title)
        item.firstName = worksheet.cell_value(curr_row,cFirstName)
        item.lastName = worksheet.cell_value(curr_row,cLastName)
        item.eMail = worksheet.cell_value(curr_row,ceMail)
        item.cellPhoneNumber = worksheet.cell_value(curr_row,cmobile)
        item.satelitePhoneNumber = worksheet.cell_value(curr_row,csatellite)
        item.officePhoneNumber  = worksheet.cell_value(curr_row,coffice)
        item.wavePhoneNumber = worksheet.cell_value(curr_row,csip)
        item.foodsat = worksheet.cell_value(curr_row,cfoodsat)
        item.sip =  worksheet.cell_value(curr_row,csip)
        item.skype  = worksheet.cell_value(curr_row,cskype)
        item.msnim = worksheet.cell_value(curr_row,cmsnim)
        item.vhfCallsign = worksheet.cell_value(curr_row,cVHFcallsign)
        item.organization = worksheet.cell_value(curr_row,cOrganization)
        item.department = worksheet.cell_value(curr_row,cDepartment)
        item.street = worksheet.cell_value(curr_row,cStreet)
        item.zip = worksheet.cell_value(curr_row,cZip)
        item.city = worksheet.cell_value(curr_row,cCity)
        item.country = worksheet.cell_value(curr_row,cCountry)
        item.jobTitle =  worksheet.cell_value(curr_row,cJobTitle)
        item.save()
        if new:
            pass


def make_place(worksheet,curr_row):
    if  worksheet.cell_value(curr_row,0) != '':
        item,new = EpicPlace.objects.get_or_create(placeID =  worksheet.cell_value(curr_row,0))
        item.compasID = worksheet.cell_value(curr_row,1)
        item.description = worksheet.cell_value(curr_row,2)
        item.type = worksheet.cell_value(curr_row,3)
        item.organization = worksheet.cell_value(curr_row,4)
        item.department = worksheet.cell_value(curr_row,5)
        item.street = worksheet.cell_value(curr_row,6)
        item.zip = worksheet.cell_value(curr_row,7)
        item.city = worksheet.cell_value(curr_row,8)
        item.country = worksheet.cell_value(curr_row,9)
        item.eMail = worksheet.cell_value(curr_row,10)
        item.phoneNumbers = worksheet.cell_value(curr_row,12)
        item.messaging = worksheet.cell_value(curr_row,12)
        try:
            item.altitude = float(worksheet.cell_value(curr_row,15))
        except:
            pass
        try:        
            item.latitude =  float(worksheet.cell_value(curr_row,16))
        except:
            pass
        try:
            item.longitude = float(worksheet.cell_value(curr_row,17))
        except:
            pass
        item.save()
        if new:
            pass
    
def make_vehicle(worksheet,curr_row):
    item,new = EpicVehicle.objects.get_or_create(vehicleID =  worksheet.cell_value(curr_row,cVehicleID))
    item.description = worksheet.cell_value(curr_row,cVehicleDescription)
    item.type = worksheet.cell_value(curr_row,cVehicleID)
    item.vhfCallsign = worksheet.cell_value(curr_row,cVehicleHfcallsign)
    item.HFCallsign = worksheet.cell_value(curr_row,cVehicleHfcallsign)
    item.licensePlate = worksheet.cell_value(curr_row,cLicensePlate)
    item.VIN = worksheet.cell_value(curr_row,cVIN)
    item.save()
    if new:
        pass
        
def make_device(worksheet,curr_row):
    item, new = EpicDevice.objects.get_or_create(deviceUid =  worksheet.cell_value(curr_row,cDeviceUID))
    item.description = worksheet.cell_value(curr_row,cDevDescription)
    item.type = worksheet.cell_value(curr_row,cDevType)
    item.capabilities =  worksheet.cell_value(curr_row,cCapabilities)
    user = worksheet.cell_value(curr_row,cDevUserID)
    vehicle = worksheet.cell_value(curr_row,cDevVehicleID)
    place = worksheet.cell_value(curr_row,cDevPlacesID)

        
    if user != "":
        try:
            usrObject = EpicUser.objects.get(username=user)
            item.owner = usrObject
        except:
            pass

    if vehicle != "":
        try:
            usrObject = EpicVehicle.objects.get(vehicleID=vehicle)
            item.vehicle = usrObject
        except:
            pass

    if place != "":
        try:
            usrObject = EpicPlace.objects.get(placeID=place)
            item.place = usrObject
        except:
            pass
    item.save()    