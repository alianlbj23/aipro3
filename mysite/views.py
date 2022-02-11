from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import *

def home(request):
    pictures = picture.objects.all()
    
    return render(request, 'index.html', locals())

