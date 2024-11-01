import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import EventForm
from .models import Events
import datetime

# Create your views here.
def home(request):
    form = EventForm()
    event_list = Events.objects.all()
    event_arr= []
    if event_list:
        for event in event_list:
            start_date = str(datetime.datetime.strptime(str(event.start_date),"%Y-%m-%d %H:%M:%S%z")) if event.start_date else None
            end_date = str(datetime.datetime.strptime(str(event.end_date),"%Y-%m-%d %H:%M:%S%z")) if event.end_date else None
            event_arr.append({'id':event.id, 'title':event.event_name, 'start': start_date , 'end':end_date})
    datatset = json.dumps(event_arr)
    return render(request, 'eventMod/index.html',{'form':form,'events':datatset})

def list_events(request):
    if request.method=='POST':
        event_list = Events.objects.all()
        event_arr= []
        if event_list:
            for event in event_list:
                start_date = event.start_date
                end_date = event.end_date
                event_arr.append({'id':event.id, 'title':event.event_name, 'start': str(datetime.datetime.strptime(str(start_date),"%Y-%m-%d %H:%M:%S%z")), 'end':str(datetime.datetime.strptime(str(end_date),"%Y-%m-%d %H:%M:%S%z"))})
        # print(event_arr)
        # return json.dumps(request, event_arr)
        return JsonResponse({json.dumps(event_arr)})


def add_events(request):

    if request.method=='POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'error':False, 'message':'Event has stored successfully.'})
        else:
            return JsonResponse({'error':True, 'message':'You have issue in form'})
    else:
        return JsonResponse({'error':True, 'message':'Method is not available'})


