from django.db import models
from datetime import datetime

# Create your models here.
class ClientDataCapture(models.Model):        
    Capture_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Capture_id')
    client_name = models.CharField(max_length=500,blank=True,null=True)
    client_system_name = models.CharField(max_length=500,blank=True,null=True)
    session_id = models.CharField(max_length=500,blank=True,null=True)
    method_name = models.CharField(max_length=500,blank=True,null=True)
    action = models.CharField(max_length=50,blank=True,null=True)
    parameter = models.CharField(max_length=5000,blank=True,null=True)
    status_code = models.CharField(max_length=500,blank=True,null=True)
    response_message = models.CharField(max_length=500,blank=True,null=True)
    row_count = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self) :
        return (self.client_name)
    class Meta:
     db_table = "ClientDataCapture"
     verbose_name = 'ClientDataCapture'
    