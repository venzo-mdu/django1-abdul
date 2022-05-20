from django.db import models
from accounts.models import User
# Create your models here.

status_choice=[
    ('in progress','in progress'),
    ('completed','completed'),
    ('paused','paused'),
    ('not started','not started')
]

class Event(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null =True)
    message = models.CharField(max_length=255,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    plannedHours = models.IntegerField(blank=True)
    consumedHours = models.IntegerField(default=0,blank=True)
    remainingHours = models.IntegerField(default=8,blank=True)
    important_message = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices = status_choice,
        default='not started',
        blank=True
    )

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-important_message']