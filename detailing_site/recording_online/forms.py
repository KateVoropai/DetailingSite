from django import forms
from .models import RecordingOnline


class AddPostForm(forms.ModelForm):

    class Meta:
        model = RecordingOnline
        fields = ['date', 'time', 'fullname', 'phone_number', 'car_number']