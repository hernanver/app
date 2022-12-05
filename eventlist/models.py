from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.admin.widgets import AdminTimeWidget

# Create your models here.

class Event(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    event_date = models.DateTimeField(null=True,blank=True)
    location = models.CharField(verbose_name="Location", max_length=50, default='')
    content = models.TextField(verbose_name="Short description", max_length=200)
    resumen = models.TextField(verbose_name="Detailed description")
    image = models.ImageField(upload_to='eventlist/files/images', height_field=None, width_field=None, max_length=None)
    link = models.CharField(verbose_name="Link", max_length=100)
    price = models.IntegerField(default=1, blank=True, null=True)
 
    class Meta:
        verbose_name= "event"
        verbose_name_plural= "events"
        ordering = ['event_date']
        

    def __str__(self):
        return self.title

