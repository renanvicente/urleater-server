#from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from app.models import Url
#from django.utils import simplejson as json
import json

# Create your views here.
def customer_page(request, slug):
  queryset = Url.objects.filter(slug=slug)
  return render_to_response('customer.html', locals(), context_instance=RequestContext(request))

def data(request):
    mimetype = 'application/json'    
    
    udata = Url.objects.all()
    sdata = []
    for d in udata:
        a = {'id': d.id, 'customer': d.slug, 'hostname': d.title,'ip': d.ip , 'urls': d.urls }
        sdata.append(a)
    return HttpResponse(json.dumps(sdata), mimetype)


def index(request):
  queryset = Url.objects.all()
  return render_to_response('overview.html', locals(), context_instance=RequestContext(request))
