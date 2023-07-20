from django.contrib import admin
from . import models

# Register your models here.

# Modify the display
class DataAdmin(admin.ModelAdmin):
    list_display = ('name','age','height','sex','predictions')
    
admin.site.register(models.Data, DataAdmin)