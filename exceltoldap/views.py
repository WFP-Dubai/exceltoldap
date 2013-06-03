from models import Document,EpicUser,EpicPlace,EpicVehicle,EpicDevice
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import DocumentForm
from utils import parse_excel

def list_documents(request):
    # Handle file upload
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            #try:
            parse_excel(newdoc)
            #except:
            print "FXCK"
            # Redirect to the document list after POST 
            return HttpResponseRedirect(reverse('exceltoldap.views.list_documents'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list_documents page
    documents = Document.objects.all()
    # Render list_documents page with the documents and the form
    return render_to_response(
        'list_documents.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def users(request):
    users = EpicUser.objects.all()
    response = render_to_response(
        'user_template.ldif',
        {'users': users},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    response['Content-Disposition'] = 'attachment; filename="users.ldif"'
    return response

def vehicles(request):
    vehicles = EpicVehicle.objects.all()
    response = render_to_response(
        'vehicle_template.ldif',
        {'vehicles': vehicles},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    #response['Content-Disposition'] = 'attachment; filename="vehicles.ldif"'
    return response
    

def places(request):
    places = EpicPlace.objects.all()
    response = render_to_response(
        'place_template.ldif',
        {'places': places},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    response['Content-Disposition'] = 'attachment; filename="places.ldif"'
    return response

def devices(request):
    dev_places = EpicDevice.objects.exclude(place = None)
    dev_vehicles = EpicDevice.objects.exclude(vehicle = None)
    dev_users = EpicDevice.objects.exclude(owner = None)
    devices = EpicDevice.objects.all() 
    response = render_to_response(
        'devices_template.ldif',
        {'devices_places': dev_places,'devices_vehicles': dev_vehicles,'devices_users': dev_users, 'devices':devices},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    response['Content-Disposition'] = 'attachment; filename="devices.ldif"'
    return response

def all_items(request):
    places = EpicPlace.objects.all()
    vehicles = EpicVehicle.objects.all()
    users = EpicUser.objects.all()   
    dev_places = EpicDevice.objects.exclude(place = None)
    dev_vehicles = EpicDevice.objects.exclude(vehicle = None)
    dev_users = EpicDevice.objects.exclude(owner = None)
    devices = EpicDevice.objects.all()      
    response = render_to_response(
        'full.ldif',
        {'places': places,'vehicles': vehicles,'users': users,'devices_places': dev_places,'devices_vehicles': dev_vehicles,'devices_users': dev_users, 'devices':devices},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    response['Content-Disposition'] = 'attachment; filename="all.ldif"'
    return response
