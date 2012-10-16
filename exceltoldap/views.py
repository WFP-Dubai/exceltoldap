from models import *
from django.views.generic.simple import direct_to_template
import xlrd
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from exceltoldap.models import Document
from exceltoldap.forms import DocumentForm
from exceltoldap.utils import *

def list(request):
    # Handle file upload
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            try:
                parse_excel(newdoc)
            except:
                pass
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('exceltoldap.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
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
    response['Content-Disposition'] = 'attachment; filename="vehicles.ldif"'
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



def all_items(request):
    places = EpicPlace.objects.all()
    vehicles = EpicVehicle.objects.all()
    users = EpicUser.objects.all()        
    response = render_to_response(
        'full.ldif',
        {'places': places,'vehicles': vehicles,'users': users},
        context_instance=RequestContext(request),
        mimetype="text/text"
    )
    response['Content-Disposition'] = 'attachment; filename="all.ldif"'
    return response
