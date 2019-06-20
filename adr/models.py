from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

# Create your models here.

# Model representing Neutral
class Neutral(models.Model):
    name = models.CharField(max_length=200, help_text='Enter neutral initial.')
    
    def __str__(self):
        return self.name

# Model representing Inquiry
class Inquiry(models.Model):
    # Unique id for the inquiry
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Inquiry')
    
    inquirer = models.CharField(max_length=200)
    
    neutral = models.ForeignKey('Neutral', on_delete=models.SET_NULL, null=True)
    
    date_inquiry = models.DateField(null=True, blank=True)
    
    follow1 = models.DateField(null=True, blank=True)
    follow2 = models.DateField(null=True, blank=True)
    
    confirmed = models.DateField(null=True, blank=True)
    notice_sent = models.DateField(null=True, blank=True)
    
    closed = models.DateField(null=True, blank=True)
    note = models.TextField(max_length=1000, help_text='Enter your note for this case.', null=True, blank=True)
    
    class Meta:
        ordering = ['date_inquiry']
        
    def __str__(self):
        return f'{self.id} ({self.neutral.name})'