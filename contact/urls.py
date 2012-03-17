#from django.conf.urls.defaults import *
#from APOLLO_PRJ.contact.models import *
#from contact.views import 

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'contact.views.ContactInfoFormHome', name='contactTemplate_main'),
	url(r'^ContactInfo/$', 'contact.views.SiteContactInfo', name = 'SiteContactInfo' )
    #url(r'^helloworld/$', 'contact.views.helloworld', name='hello_world'),
    #url(r'^sign_up/$', 'contact.views.ContactInfoFormSub', name='ContactInfoFormSub'),
    #url(r'^hello$', 'contact.views.hello', name='hello'),
)
