from django.contrib import admin
from .models import Event, MakeReservation

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'start_time', 'end_time', 'is_recurring','is_private','recurrence_day','is_expired')
    list_filter = ('is_recurring', 'recurrence_day','is_private')
    search_fields = ('title',)

@admin.register(MakeReservation)
class MakeRservationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email_address', 'event', 'Gender')
    list_filter = ('Gender', 'event')
    search_fields = ('event',)
