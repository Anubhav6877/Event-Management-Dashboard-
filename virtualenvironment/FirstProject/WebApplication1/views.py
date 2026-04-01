from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from .forms import EventForm
from django.contrib.auth.decorators import login_required

def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


@login_required
def create_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        return redirect('home')
    return render(request, 'create_event.html', {'form': form})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    #Check if user already registered
    already_registered=False
    if request.user.is_authenticated:already_registered=Registration.objects.filter(user=request.user,event=event).exists()
    count = Registration.objects.filter(event=event).count()
    return render(request, 'event_detail.html', {'event': event, 'count': count,'already_registered':already_registered})


@login_required
def register_event(request, id):
    event = get_object_or_404(Event, id=id)

    #Prevent Duplicate Registration
    if not Registration.objects.filter(user=request.user, event=event).exists():
        Registration.objects.create(user=request.user,event=event)
    return redirect('event_detail',id=id)
    
