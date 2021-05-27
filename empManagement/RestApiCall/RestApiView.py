# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .RestApiModels import ToDo
from .RestApiSerializers import ToDoSerializer
from rest_framework import serializers, status
from rest_framework import viewsets
import requests
from requests.exceptions import HTTPError
URL = 'https://jsonplaceholder.typicode.com/todos'


class ToDoViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            print('Request operation Initiated')
            queryset = requests.get(URL)
            # print(queryset.json())
            serializer = ToDoSerializer(queryset.json(), many=True)
            print(serializer)
            return Response(serializer.data)

        except HTTPError as http_err:
            Response(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            Response(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
        finally:
            print('Request operation completed')

    def retrieve(self, request, pk=None):

        try:
            id = pk
            if id is not None:
                newURL = f'{URL}/{id}'
                print(newURL)
                queryset = requests.get(newURL)
                serializer = ToDoSerializer(queryset.json())
                # print(serializer)
                return Response(serializer.data)
        except HTTPError as http_err:
            Response(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            Response(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
        finally:
            print('Request operation completed')

    # def create(self, request):

    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):

    #     id = pk
    #     stu = Employee.objects.get(pk=id)
    #     serializer = EmployeeSerializer(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer.data)
    #         return Response({'msg': 'Complete Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk):

    #     e_id = pk
    #     stu = Employee.objects.get(pk=e_id)
    #     serializer = EmployeeSerializer(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Partial Data Updated'})
    #     return Response(serializer.errors)

    # def destroy(self, request, pk):

    #     id = pk
    #     stu = Employee.objects.get(pk=id)
    #     stu.delete()
    #     return Response({'msg': 'Data Deleted'})
