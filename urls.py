import os.path


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url
#from contact.views import current_datetime
from django.contrib import admin 



admin.autodiscover()

stylesheets = os.path.join(os.path.dirname(__file__), "stylesheets")


urlpatterns = patterns('',

    url(r'^$', 'contact.views.home', name='home'),
    url(r'^contactTemplate/', include('contact.urls')),
    
    url(r'^$', 'census.views.home', name='home'),
    url(r'^censusTemplate/', include('census.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^stylesheets/(?P<path>.*)$','django.views.static.serve', { 'document_root' : stylesheets}),
    )

urlpatterns += staticfiles_urlpatterns()



    # url(r'^signup/', include('signupform.urls')),
    # url(r'^gameshow/', include('gameshow.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),