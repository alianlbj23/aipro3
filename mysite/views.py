from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http.response import FileResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import BookForm
from .models import *
from django.core.files import File

import zipfile
from django.conf.urls.static import static
import shutil
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import listdir
from aipro3 import settings
from django.utils.encoding import escape_uri_path#處理下載檔名不能用中文命名的問題
from django.conf import settings
def home(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    return render(request, 'index.html', locals())


def tool(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    #zip_download = ZipFile.objects.filter(packeage_name="傲慢與偏見")
    return render(request, 'tool.html', locals())

def tool2(request):
    pictures = picture.objects.all()
    student_width = '95.7%'
    #teacher_width = '100%'
    return render(request, 'tool2.html', locals())

def zip_download(request, file_name):
    file_path='static1/zip_file/'+str(file_name)+'.zip'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    fileName = file_name
    response['Content-Disposition'] = 'attachment;filename={0}'.format(escape_uri_path(fileName))+".zip"
    return response

