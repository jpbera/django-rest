from rest_framework import serializers
from .models import Employee,Company,Client

class CompanySerializer(serializers.ModelSerializer):
 class Meta:
  model = Company 
  fields = ['c_id','c_name', 'c_address']

class EmployeeSerializer(serializers.ModelSerializer):
#  company=CompanySerializer(many=True, required=False)
 class Meta:
  model = Employee 
  fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
#  company=CompanySerializer(many=True, required=False)
 class Meta:
  model = Client 
  fields = '__all__'
