from django.contrib import admin

from .models import Client, Employee,Company
from .ClientDataCapture.ClientDataTrackingModels import ClientDataCapture
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
 list_display  = ['e_name', 'e_phone', 'e_address', 'e_pic','e_email','c_name']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
 list_display  = ['c_id','c_name', 'c_address']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
 list_display  = ['client_id','client_name']

@admin.register(ClientDataCapture)
class ClientDataCaptureAdmin(admin.ModelAdmin):
    list_display  = ['Capture_id','client_name', 'client_system_name','session_id',
                     'method_name','action','parameter' ,'status_code','response_message',
                     'row_count', 'created_date']
  
