from rest_framework import serializers
from .ClientDataTrackingModels import ClientDataCapture

class ClientDataCaptureSerializer(serializers.ModelSerializer):
 class Meta:
  model = ClientDataCapture 
  fields = ['Capture_id','client_name', 'client_system_name','session_id',
            'method_name','action','parameter' ,'status_code','response_message',
            'row_count', 'created_date']
  