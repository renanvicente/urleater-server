from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urleater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'api/data', 'app.views.data'),
    url(r'^$', 'app.views.index'),
    url(r'^customers/(?P<slug>[-\w]+)/$', 'app.views.customer_page'),
    url(r'^generate_csv$', 'app.views.get_csv'),
    url(r'^export_zabbix$', 'app.views.export_zabbix'),
    url(r'^admin/', include(admin.site.urls)),
)
