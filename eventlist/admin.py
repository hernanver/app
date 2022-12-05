from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields= ('id',)
  

    
admin.site.register(Event, EventAdmin)