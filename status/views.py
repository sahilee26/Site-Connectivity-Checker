from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import query, uquery
import requests

from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from django.core.paginator import Paginator
import time
from threading import Thread
from datetime import datetime



http_code = {
	100: "Continue",
	101: "Switching Protocols",
	103: "Checkpoint",
	200: "OK",
	201: "Created",
	202: "Accepted",
	203: "Non-Authoritative Information",
	204: "No Content",
	205: "Reset Content",
	206: "Partial Content",
	300: "Multiple Choices",
	301: "The Requested Page has moved permanently to a new URL",
	302: "The Requested Page has moved temporarily to a new URL",
	303: "The Requested Page can be found under a different URL",
	304: "Not Modified",
	306: "Switch Proxy: No longer used",
	400: "Bad Request",
	401: "Unauthorized",
	402: "Payment required",
	403: "Forbidden",
	404: "Not Found",
	408: "Request Timeout",
	500: "Internal Server Error",
	501: "Not Implemented",
	502: "Bad Gateway",
	503: "Service Unavailable",
	504: "Gateway Timeout"
}


def index(request):
	return render(request, 'index.html')

def insights(request):
	pageSize = 10
	response=query.objects.all().order_by('-timeq')
	paginator = Paginator(response, pageSize)

    # Get page parameter from query and render that particular page
    # Defaults to the 1st page
	page = request.GET.get('page', 1)
	finalResponse = paginator.get_page(page)
	template = loader.get_template('insights.html')
	return HttpResponse(template.render({'data': finalResponse}, request))



def trackurl(url, source):
	while(True):
		response=uquery.objects.all().order_by('-timeq')
		bh = response.filter(urlq=url).first()
		if bh.startq=='False':
			break
		for key in http_code.keys():	
			if source.status_code==key:
				query.objects.create(
				urlq = url,
				messageq = http_code[key],
				statusq = key,
				timeq = datetime.now()
				)
		time.sleep(25)

def status(request):
	url=request.POST['url']
	start1=request.POST.get('start')

	if url[:4] != "http" :
		return render(request, "cross.html", {'message':"Invalid URL"})
	try:
		source=requests.get(url)
	except:
		return render(request,"cross.html",{'message':"The Site can't be reached."})
	if start1=='True':
		uquery.objects.create(
			urlq = url,
			startq = 'True',
			timeq=datetime.now()
		)
		process = Thread(target=trackurl, args=(url, source))
		process.start()
		response = {
					"success": True,
					"message": "A background asynchronorous job to track URL status has been triggered. Please check results on page localhost:8000/insights"
					}
		return JsonResponse(response)

	else:
		bh=uquery.objects.filter(urlq=url).first()
		bh.startq='False'
		bh.save()
		response = {
				"success": True,
				"message": "A background asynchronorous job to track URL status has been switched off"
		}
		return JsonResponse(response)
