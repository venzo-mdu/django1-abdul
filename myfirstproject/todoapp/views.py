from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Event


# Create your views here.
def event_update(request,pk):
    object = Event.objects.get(id=pk)
    form = EventForm(instance=object)
    if request.method == 'POST':
        form = EventForm(request.POST,instance=object)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.remainingHours = obj.plannedHours - obj.consumedHours
            obj = form.save()
            return redirect('/events')
    context = {'form':form}
    return render(request,'todoapp/eventupdate.html',context)

def event_delete(request,pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('/events')
    context = {}
    return render(request,'todoapp/eventdelete.html',context)

@login_required(login_url='/login')
def event_view(request):
    events = Event.objects.filter(user = request.user)
    progress = events.filter(status = 'in progress').count
    completed = events.filter(status = 'completed').count
    paused =  events.filter(status = 'paused').count
    not_started = events.filter(status = 'not started').count
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.remainingHours = event.plannedHours
            event = form.save()
            return redirect('/events')
        else:
            messages.error(request,form.errors)

    context={'events':events,'form':form,'progress':progress,'completed':completed,'paused':paused,'not_started':not_started}
    return render(request,'todoapp/Events.html',context)
