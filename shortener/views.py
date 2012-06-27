from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from shortener.models import *

def new(request):
	if request.method == 'POST': # If the form has been submitted...
		form = URLForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			assoc = form.save()
			return HttpResponseRedirect(reverse('url_detail', args=(assoc.id,))) # TODO redirect to url_detail page
	else:
		form = URLForm()

	return render_to_response('shortener/new.html', {
		'form': form,
	}, RequestContext(request))

def url_detail(request, id):
	a = get_object_or_404(URLAssociation, pk=id)
	return render_to_response('shortener/url_detail.html', {
		'association': a,
		'short_url': request.build_absolute_uri( reverse('redirect', args=(a.code(),) )),
	}, RequestContext(request))

def redirect(request, code):
	try:
		url = URLAssociation.get_from_code(code).actual_url
		return HttpResponseRedirect(url)
	except URLAssociation.DoesNotExist:
		return HttpResponse("URL not registered")
