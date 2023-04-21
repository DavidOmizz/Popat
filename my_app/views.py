
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from datetime import datetime
from .forms import MakeReservationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event
from .forms import MakeReservationForm


def index(request):
    today = datetime.today()
    # events_today = Event.objects.filter(start_date__lte=today, end_date__gte=today, is_recurring=False)
    

     # Filter recurring events that occur on the current day of the week
    current_time = datetime.now().time()
    
    events_today = Event.objects.filter(start_date__lte=today, end_date__gte=today, is_recurring=False,start_time__lte=current_time,
        end_time__gte=current_time)

    current_day_of_week = today.strftime('%A')
    recurring_events_today = Event.objects.filter(
        is_recurring=True,
        recurrence_day=today.strftime('%A'),
        start_time__lte=datetime.now().time(),
        end_time__gte=datetime.now().time(),
    )
    context = {
        'events_today': events_today,
        'recurring_events_today': recurring_events_today
    }
    return render(request, 'index.html', context)

# def EventDetail(request, pk):
#     # event = Event.objects.get(id=pk)
#     event = get_object_or_404(Event, id=pk)
#     template_name = 'event.html'
#     rsvp = None
#     if request.method =='POST':
#         orders = MakeReservationForm(data=request.POST)
#         if orders.is_valid():
#             rsvp = orders.save(commit=False)
#             rsvp.event = event
#             rsvp.save()
#             messages.success(request,'Order Placed succesffully')
#             # return render(request, '')
#             return redirect(request.path_info)
#     else:
#         orders = MakeReservationForm()
#     return render(request, template_name, {'event':event, 'orders':orders, 'rsvp':rsvp})


# def EventDetail(request, pk):
#     event = Event.objects.get(id=pk)
#     template_name = 'event.html'
#     rsvp = None
#     if request.method =='POST':
#         orders = MakeReservationForm(data=request.POST)
#         if orders.is_valid():
#             rsvp = orders.save(commit=False)
#             # check if event is private
#             if event.is_private:
#                 private_password = request.POST.get('private_password')
#                 if private_password != event.private_password:
#                     # password is incorrect, return form with error message
#                     orders.add_error('private_password', 'Incorrect password')
#                     return render(request, template_name, {'event':event, 'orders':orders, 'rsvp':rsvp})
#             rsvp.post = event
#             rsvp.save()
#             messages.success(request,'Order Placed successfully')
#     else:
#         orders = MakeReservationForm()
#     return render(request, template_name, {'event':event, 'orders':orders, 'rsvp':rsvp})


def EventDetail(request, pk):
    event = get_object_or_404(Event, id=pk)
    template_name = 'event.html'
    reservation = None
    if event.is_private:
        # If the event is private, check if the user entered the correct password
        if request.method == 'POST':
            form = MakeReservationForm(request.POST)
            if form.is_valid():
                private_password = form.cleaned_data.get('private_password')
                if private_password != event.private_password:
                    form.add_error('private_password', 'Incorrect password')
                    return render(request, template_name, {'event': event, 'form': form})
                else:
                    # Password is correct, create reservation and redirect to confirmation page
                    reservation = form.save(commit=False)
                    reservation.event = event
                    reservation.save()
                    return redirect(request.path_info)
                    # return HttpResponseRedirect(reverse('reservation_confirmation', args=(reservation.pk,)))
        else:
            form = MakeReservationForm()
            return render(request, 'event.html', {'event': event, 'form': form})
    else:
        # If the event is not private, create reservation and redirect to confirmation page
        if request.method == 'POST':
            form = MakeReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.event = event
                reservation.save()
                return redirect(request.path_info)
                # return HttpResponseRedirect(reverse('reservation_confirmation', args=(reservation.pk,)))
        else:
            form = MakeReservationForm()
    return render(request, template_name, {'event': event, 'form': form})



