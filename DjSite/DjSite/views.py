'''
Created on Dec 18, 2016

@author: Admin
'''
from django.http import HttpResponse
import datetime
import django
from django.shortcuts import render_to_response
import mysql



def current_time(request):    
    now = datetime.datetime.now()
    htmlContent = "<html><head></head><body> Current time =%s</body></html>"%now
    return render_to_response('BooksList.html', {'name':'AjayKumar'})



def search(request):
    print('GET called')
    print(request.POST)
    htmlContent = "<html><head></head><body> welcome</body></html>"
    return HttpResponse(htmlContent)