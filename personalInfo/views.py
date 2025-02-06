from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def personalInfo(request):
    template = loader.get_template('personalInfo.html')
    return HttpResponse(template.render())



