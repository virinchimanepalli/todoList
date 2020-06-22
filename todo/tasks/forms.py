from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    # title

    class Meta:
        model = Task
        fields = '__all__'
