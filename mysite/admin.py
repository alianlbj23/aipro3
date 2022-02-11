from django.contrib import admin
from mysite.models import *
# Register your models here.
class pictureAdmin(admin.ModelAdmin):
    list_display = ['image']
admin.site.register(picture, pictureAdmin)