from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import *

def home(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    return render(request, 'index.html', locals())


def tool(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    return render(request, 'tool.html', locals())

def tool2(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    return render(request, 'tool2.html', locals())

