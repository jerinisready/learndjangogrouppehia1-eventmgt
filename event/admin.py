from django.contrib import admin

# Register your models here.
from event.models import Event, Registration

admin.site.register(Event)
admin.site.register(Registration)
