from django.contrib import admin
from mysite.models import *
# Register your models here.
class pictureAdmin(admin.ModelAdmin):
    list_display = ['image']
admin.site.register(picture, pictureAdmin)

class ZipFileAdmin(admin.ModelAdmin):
    list_display = ['packeage_name','zip_file']
admin.site.register(ZipFile, ZipFileAdmin)