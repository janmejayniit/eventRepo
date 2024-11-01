from django.contrib import admin
from .models import Events

# Register your models here.
class EventAdmin(admin.ModelAdmin):
  list_display = ('event_name','start_date','end_date')

admin.site.register(Events, EventAdmin)