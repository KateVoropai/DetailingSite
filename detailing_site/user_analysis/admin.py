from django.contrib import admin
from .models import UserAnalysis

@admin.register(UserAnalysis)
class UserAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'fullname', 'phone_number')

