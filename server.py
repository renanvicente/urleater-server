#!/usr/bin/env python
from SocketServer import ThreadingTCPServer, BaseRequestHandler
from app.models import Url
from json import loads, dumps

class TCPServer(ThreadingTCPServer):
  allow_reuse_address = True


class TCPServerHandler(BaseRequestHandler):
   """
   Reveice data to insert in URLEater
   """
   def handle(self):
       """
       Handle TCP datagrams
       """

       data = loads(self.request.recv(1024).strip())

       print "Recebido de '%s': %s \n" % (self.client_address[0], data)
       try:
         obj = Url.objects.filter(title=data['hostname']).update(ip=data['ip'],urls=data['urls'],slug=data['customer'])
         if obj:
           self.request.sendall(dumps({'return':'Successfully updated'}))
         else:
           obj = Url(title=data['hostname'],ip=data['ip'],urls=data['urls'],slug=data['customer'])
           obj.save()
           self.request.sendall(dumps({'return':'Successfully created'}))
       except Url.DoesNotExist:
         obj = Url(title=data['hostname'],ip=data['ip'],urls=data['urls'],slug=data['customer'])
         obj.save()
         self.request.sendall(dumps({'return':'Successfully created'}))


if __name__ == "__main__":
   import os
   os.environ['DJANGO_SETTINGS_MODULE'] = 'urleater.settings'
   #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urleater.settings")
   listen_host = "0.0.0.0"
   listen_port = 7777

   print "Starting URLEater server on '%s:%s'...\n" % (listen_host, listen_port)

   server = TCPServer((listen_host, listen_port), TCPServerHandler)
   server.serve_forever()
