from django.conf.urls.defaults import patterns, url
from views import CensusInfoHome, SiteCensusInfo

urlpatterns = patterns('',
	url(r'^$', 'census.views.CensusInfoHome', name='censusTemplate_main'),
	url(r'^SiteCensusInfo/$', 'census.views.SiteCensusInfo', name = 'SiteCensusInfo' )
   
)
