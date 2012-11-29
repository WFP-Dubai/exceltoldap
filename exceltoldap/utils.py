from models import EpicUser, EpicPlace, EpicVehicle,EpicDevice
import datetime
import xlrd

def parse_excel(uploaded_file):
    # read file
    # Check file correct file
    # open Excel
    
    workbook = xlrd.open_workbook(uploaded_file.docfile.name)
    
    #Call import users
    users = workbook.sheet_by_name('Users')
    import_users(users)
    places = workbook.sheet_by_name('Places')
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
        try:
            make_place(worksheet,curr_row)
        except:
            pass

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
        item.phoneNumbers = worksheet.cell_value(curr_row,5)
        item.foodsat = worksheet.cell_value(curr_row,6)
        # 7 VHF callsign
        item.vhfCallsign = worksheet.cell_value(curr_row,7)
        item.organization = worksheet.cell_value(curr_row,8)
        item.department = worksheet.cell_value(curr_row,9)
        item.street = worksheet.cell_value(curr_row,10)
        item.zip = worksheet.cell_value(curr_row,11)
        item.city = worksheet.cell_value(curr_row,12)
        item.country = worksheet.cell_value(curr_row,13)
        item.jobTitle =  worksheet.cell_value(curr_row,14)
        item.save()
        if new:
            pass
    except:
        pass
    

def make_place(worksheet,curr_row):
    if 
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
    item.phoneNumbers = worksheet.cell_value(curr_row,11)
    item.messaging = worksheet.cell_value(curr_row,12)
    item.altitude = worksheet.cell_value(curr_row,13)
    item.latitude =  worksheet.cell_value(curr_row,14)
    item.longitude = worksheet.cell_value(curr_row,15)
    d_id = worksheet.cell_value(curr_row,16)
    if d_id:
        device, new = EpicDevice.objects.get_or_create(deviceUid=d_id,Description="Radio For "+item.vehicleID,Capabilities="gps")
        item.deviceID =  device
    item.save()
    if new:
        pass
    
def make_vehicle(worksheet,curr_row):
    item,new = EpicVehicle.objects.get_or_create(vehicleID =  worksheet.cell_value(curr_row,0))
    item.description = worksheet.cell_value(curr_row,1)
    item.type = worksheet.cell_value(curr_row,2)
    item.messaging = worksheet.cell_value(curr_row,3)
    item.licensePlate = worksheet.cell_value(curr_row,4)
    item.VIN = worksheet.cell_value(curr_row,5)
    #make or link device
    d_id = worksheet.cell_value(curr_row,6)
    if d_id:
        device, new = EpicDevice.objects.get_or_create(deviceUid=d_id,Description="Radio For "+item.vehicleID,Capabilities="gps")
        item.deviceID =  device
    item.save()
    if new:
        pass
    