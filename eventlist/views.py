from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Event
from django.http import Http404, HttpResponse
from datetime import datetime

# Create your views here.



def detail(request, event_id):
    eventdetail = Event.objects.get(pk=event_id)

    if eventdetail is not None:
        return render(request, 'eventlist/eventlist_detail.html', {'event': eventdetail})
    else:
        raise Http404('El evento no existe')

class EventListView(ListView):
    model = Event
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context