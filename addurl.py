import pathlib
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aipro3.settings')
django.setup()
from mysite.models import *

path = str(pathlib.Path(__file__).parent.absolute()) + '\static1\picture'
dirlist = os.listdir(path) #取得path路徑下的所有檔案 
for i in dirlist:
    url = '/static1/picture/'+str(i)
    
    new = picture.objects.create(image=url)
    new.save()