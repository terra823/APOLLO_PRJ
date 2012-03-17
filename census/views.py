from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages

from models import CensusInfo
#from census.forms import CensusInfo
from forms import CensusInfoForm


def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))    


def CensusInfoHome(request):
 	oursite = get_current_site(request)
 	return render_to_response('censusTemplate/main.html' , {'title': oursite.name}, context_instance=RequestContext(request))


def SiteCensusInfo(request):
    if request.method == 'POST':
        form = CensusInfoForm(request.POST, request.FILES)
        if form.is_valid(): #and form.is_multipart():
            form.save()
            messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
            return redirect('censusTemplate_main')
    else:
        form = CensusInfoForm()
    return render_to_response('censusTemplate/censussubmission.html', {'form': form}, context_instance=RequestContext(request))


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)