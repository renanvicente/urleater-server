from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from app.models import Url
from json import dumps
from djqscsv import render_to_csv_response
import csv

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
    return HttpResponse(dumps(sdata), mimetype)


def index(request):
  queryset = Url.objects.all()
  return render_to_response('overview.html', locals(), context_instance=RequestContext(request))


def get_csv(request):
  queryset = Url.objects.all()
  return render_to_csv_response(queryset)

def export_zabbix(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="export_zabbix.csv"'
  writer = csv.writer(response)
  queryset = Url.objects.all()
  for d in queryset:
    urls = str(d.urls).split(' ')
    for url in urls:
      if url is not '':
        try:
          name = "Site " + url.split('.')[0]
          writer.writerow([ name, url, name ])
        except Exception, e:
          pass
  return response
