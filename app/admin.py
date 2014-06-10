from django.contrib import admin
from app.models import *
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
  pass

admin.site.register(Url,UrlAdmin)
