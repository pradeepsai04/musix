from django.contrib import admin
from .models import upload,data

# Register your models here.
admin.site.register(upload)


@admin.register(data)
class diaplaydata(admin.ModelAdmin):
    list_display=['name','age']

