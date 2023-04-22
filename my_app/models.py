from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

Gender = [
    ('male','male'),
    ('female','female')
]

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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_private = models.BooleanField(default=False)
    private_password = models.CharField(max_length=255, null=True, blank=True)
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


class MakeReservation(models.Model):
    event = models.ForeignKey(Event, verbose_name='Event', on_delete=models.CASCADE)
    Name = models.CharField(verbose_name='First Name', max_length=255)
    Email_address = models.EmailField()
    Confirm_address = models.EmailField(null=True)
    Number_of_guest = models.IntegerField(null=True)
    Gender = models.CharField(max_length=255, choices=Gender)
    
    def __str__(self):
       return self.Name
   