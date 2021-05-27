from rest_framework import serializers
from .RestApiModels import ToDo

class ToDoSerializer(serializers.ModelSerializer):
 class Meta:
  model = ToDo 
  fields = ['id','userId', 'title','completed']