from django.db import models

class Url(models.Model):
  '''Hostname and urls'''
  title    = models.CharField( max_length=100, )
  ip       = models.CharField( max_length=100, )
  urls     = models.CharField( max_length=500, )
  slug     = models.SlugField()
  
  def __unicode__(self):
    return u'%s' % self.title

#  class Meta:
#    ordering = ['slug']
