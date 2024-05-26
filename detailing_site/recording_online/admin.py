from django.contrib import admin
from .models import RecordingOnline

@admin.register(RecordingOnline)
class RecordingOnlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'fullname', 'phone_number')
    list_display_links = ('id', 'fullname', 'phone_number')
    ordering = ['date', 'time']

