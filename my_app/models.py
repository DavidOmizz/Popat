from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    price = models.CharField(max_length = 255,null=True)
    description = models.CharField(max_length = 255,null=True)
    location = models.CharField(max_length = 255, null =True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_private = models.BooleanField(default=False)
    is_recurring = models.BooleanField(default=False)
    recurrence_day = models.CharField(max_length=10, null=True, blank=True, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.title

    def is_today(self):
        return self.start_date <= timezone.now().date() <= self.end_date

    def is_recurring_today(self):
        if not self.is_recurring:
            return False
        return timezone.now().strftime('%A') == self.recurrence_day

    def is_expired(self):
        end_datetime = timezone.make_aware(
            timezone.datetime.combine(self.end_date, self.end_time)
        )
        return timezone.now() > end_datetime
    
    def is_expired(self):
        end_datetime = timezone.make_aware(
            timezone.datetime.combine(self.end_date, self.end_time)
        )
        return timezone.now() > end_datetime
