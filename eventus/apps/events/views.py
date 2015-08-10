from django.shortcuts import render, redirect
from .models import Event, Category
from .forms import EventoForm
from apps.users.models import User

from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    events = Event.objects.all().order_by('-created')[:6]
    categories = Category.objects.all()
    #print events
    #print categories
    return render(request, 'events/index.html', {'events' : events, 'category' : categories})
    

def main_panel(request):
    #events = Event.objects.filter(organizer__username = 'wilzonmj').order_by('is_free', '-created')
    events = Event.objects.order_by('is_free', '-created')
    cantidad_eventos = eventos = events.count()
    return render(request, 'events/panel/panel.html', {'events' : events, 'cantidad' : cantidad_eventos})


def crear_evento(request):
    if request.method == 'POST':
        modelform = EventoForm(request.POST, request.FILES)
        if modelform.is_valid():
            organizador = User.objects.get(pk = 1)
            nuevo_evento = modelform.save()
            nuevo_evento.organizer = organizador
            nuevo_evento.save()
            return redirect(reverse('events_app:panel'))
    else:
        modelform = EventoForm()

    return render(request, 'events/panel/crear_evento.html', {'form' : modelform})
