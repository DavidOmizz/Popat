from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'start_time', 'end_time', 'is_recurring','is_private','recurrence_day','is_expired')
    list_filter = ('is_recurring', 'recurrence_day','is_private')
    search_fields = ('title',)