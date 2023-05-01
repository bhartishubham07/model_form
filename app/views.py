from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    TFO = TopicForm()
    d = {'TFO' : TFO}
    
    if request.method == 'POST':
        TFD = TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic data inserted Successfully')
    
    return render(request, 'insert_topic.html', d)



def insert_webpage(request):
    WFO = WebpageForm()
    d = {'WFO' : WFO}
    
    if request.method == 'POST':
        WPFD = WebpageForm(request.POST)
        if WPFD.is_valid():
            WPFD.save()
            return HttpResponse('Webpage data inserted Successfully')
    
    return render(request, 'insert_webpage.html', d)



def insert_record(request):
    AFO = AccessForm()
    d = {'AFO' : AFO}
    
    if request.method == 'POST':
        AFD = AccessForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('Access Data Inserted successfully')
    
    return render(request, 'insert_record.html', d)
    
    
    
    
    
    
    
    
    
    