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

def home(request):
    template = "home.html"
    return direct_to_template(request, template)


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            #parse_excel(newdoc)
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
    pass
    
def vehicles(request):
    pass
    
def places(request):
    pass

def all_items(request):
    pass
    
