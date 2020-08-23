# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
#from edxmako.shortcuts import render_to_response

# Create your views here.
def getAboutUs(request):
    return render_to_response('AboutUs.html')

def getMobileApp(request,os):
    if os =='app_store':
        return render_to_response('app_store.html')
    else :
        return render_to_response('play_store.html')
    