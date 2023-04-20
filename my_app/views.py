
from django.shortcuts import render
from .models import Event
from datetime import datetime

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

