from dataclasses import fields
import imp
from socket import fromshare
from django import forms
from django.forms import ModelForm
from . models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'

