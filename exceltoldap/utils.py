from exceltoldap.models import *
import xlrd

def parse_excel(file):
    # read file
    # Check file correct file
    # open Excel
    workbook = xlrd.open_workbook(file.docfile.name)
    
    # Call import users
    users = workbook.sheet_by_name('Users')
    import_users(users)
    return True
    

def import_users(worksheet):
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = 1
    while curr_row < num_rows:
        curr_row += 1
        username = worksheet.cell_value(curr_row,0)
        personalTitle = worksheet.cell_value(curr_row,1)
        firstName = worksheet.cell_value(curr_row,2)
        lastName = worksheet.cell_value(curr_row,3)
        eMail = worksheet.cell_value(curr_row,4)
        additionalEmails = worksheet.cell_value(curr_row,5)
        phoneNumbers = worksheet.cell_value(curr_row,6)
        messaging = worksheet.cell_value(curr_row,7)
        organization = worksheet.cell_value(curr_row,8)
        department = worksheet.cell_value(curr_row,9)
        street = worksheet.cell_value(curr_row,10)
        zip = worksheet.cell_value(curr_row,11)
        city = worksheet.cell_value(curr_row,12)
        country = worksheet.cell_value(curr_row,13)
        jobTitle = worksheet.cell_value(curr_row,14)
        preferredLanguage = worksheet.cell_value(curr_row,15)
        deviceID= worksheet.cell_value(curr_row,16)
        
        user,new = EpicUser.objects.get_or_create(username =  username)
        user.personalTitle = personalTitle
        user.firstName=firstName
        user.lastName=lastName
        user.eMail=eMail
        user.additionalEmails=additionalEmails
        user.phoneNumbers=phoneNumbers
        user.messaging=messaging
        user.organization=organization
        user.department=department
        user.street=street
        user.zip=zip
        user.city=city
        user.country=country
        user.jobTitle=jobTitle
        user.preferredLanguage=preferredLanguage
        user.save()
    return True

def import_places(worksheet):
    #read sheet
    #parse
    
    return a
    
    
def import_vehicles(worksheet):
    #read sheet
    #parse
    # save

    return a
