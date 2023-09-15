from django.contrib import admin

# Register your models here.
from .models import *
class Csvrequestadmin(admin.ModelAdmin):
    list_display=["id","num_records","new_file_name"]
admin.site.register(CSVRequest,Csvrequestadmin)