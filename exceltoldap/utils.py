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
        make_user(worksheet,curr_row)
    return True


def import_places(worksheet):
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = 1
    while curr_row < num_rows:
        curr_row += 1
        make_user(worksheet,curr_row)

    return True
    
    
def import_vehicles(worksheet):
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = 1
    while curr_row < num_rows:
        curr_row += 1
        make_user(worksheet,curr_row)

    return True


def make_user(worksheet,row):
#	deviceID= worksheet.cell_value(curr_row,16)	
	item,new = EpicUser.objects.get_or_create(username =  worksheet.cell_value(curr_row,0))
	item.personalTitle = worksheet.cell_value(curr_row,1)
	item.firstName = worksheet.cell_value(curr_row,2)
	item.lastName = worksheet.cell_value(curr_row,3)
	item.eMail = worksheet.cell_value(curr_row,4)
	item.additionalEmails = worksheet.cell_value(curr_row,5)
	item.phoneNumbers = worksheet.cell_value(curr_row,6)
	item.messaging = worksheet.cell_value(curr_row,7)
	item.organization = worksheet.cell_value(curr_row,8)
	item.department = worksheet.cell_value(curr_row,9)
	item.street = worksheet.cell_value(curr_row,10)
	item.zip = worksheet.cell_value(curr_row,11)
	item.city = worksheet.cell_value(curr_row,12)
	item.country = worksheet.cell_value(curr_row,13)
	item.jobTitle =  worksheet.cell_value(curr_row,14)
	item.preferredLanguage = worksheet.cell_value(curr_row,15)
	item.save()

