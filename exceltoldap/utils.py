from models import EpicUser, EpicPlace, EpicVehicle,EpicDevice
import datetime
import xlrd
import settings


def parse_excel(uploaded_file):
    # read file
    # Check file correct file
    # open Excel
    
    workbook = xlrd.open_workbook(settings.MEDIA_ROOT + uploaded_file.docfile.url)
    
    #Call import users
    users = workbook.sheet_by_name(u'Users')
    import_users(users)
    places = workbook.sheet_by_name(u'Places')
    import_places(places)
    vehicles = workbook.sheet_by_name(u'Vehicles')
    import_vehicles(vehicles)
    
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
        try:
            make_user(worksheet,curr_row)
        except:
            pass
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


def make_user(worksheet,curr_row):
    if worksheet.cell_value(curr_row,0) != '':
        item,new = EpicUser.objects.get_or_create(username =  worksheet.cell_value(curr_row,0))
        item.personalTitle = worksheet.cell_value(curr_row,1)
        item.firstName = worksheet.cell_value(curr_row,2)
        item.lastName = worksheet.cell_value(curr_row,3)
        item.eMail = worksheet.cell_value(curr_row,4)
        item.cellPhoneNumber = worksheet.cell_value(curr_row,5)
        item.satelitePhoneNumber = worksheet.cell_value(curr_row,6)
        item.officePhoneNumber  = worksheet.cell_value(curr_row,7)
        item.wavePhoneNumber = worksheet.cell_value(curr_row,8)
        item.foodsat = worksheet.cell_value(curr_row,9)
        item.sip =  worksheet.cell_value(curr_row,10)
        item.skype  = worksheet.cell_value(curr_row,11)
        item.msnim = worksheet.cell_value(curr_row,12)
        item.vhfCallsign = worksheet.cell_value(curr_row,13)
        item.organization = worksheet.cell_value(curr_row,14)
        item.department = worksheet.cell_value(curr_row,15)
        item.street = worksheet.cell_value(curr_row,16)
        item.zip = worksheet.cell_value(curr_row,17)
        item.city = worksheet.cell_value(curr_row,18)
        item.country = worksheet.cell_value(curr_row,19)
        item.jobTitle =  worksheet.cell_value(curr_row,20)
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
    item,new = EpicVehicle.objects.get_or_create(vehicleID =  worksheet.cell_value(curr_row,0))
    item.description = worksheet.cell_value(curr_row,1)
    item.type = worksheet.cell_value(curr_row,2)
    item.vhfCallsign = worksheet.cell_value(curr_row,3)
    item.HFCallsign = worksheet.cell_value(curr_row,4)
    item.licensePlate = worksheet.cell_value(curr_row,5)
    item.VIN = worksheet.cell_value(curr_row,6)
    #make or link device
    d_id = worksheet.cell_value(curr_row,6)
    if d_id:
        try:
            device, new = EpicDevice.objects.get_or_create(deviceUid=d_id,Description="Radio For "+item.vehicleID,Capabilities="gps")
            item.deviceID =  device
        except:
            pass
    item.save()
    if new:
        pass
    