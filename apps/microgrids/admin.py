# Register your models here.
from django.contrib import admin
from .models import Img

@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_h', 'img')
