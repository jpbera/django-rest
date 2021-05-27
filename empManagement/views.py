# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee,Client
from .serializers import EmployeeSerializer,ClientSerializer
from rest_framework import status
from rest_framework import viewsets
from .Middleware.clientValidation import ClientValidation, fnClientDataCapture
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# ctrl + / comment line

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


# http://127.0.0.1:8000/employeeapi/?user_id=1&location=uk
class EmployeeViewSet(viewsets.ViewSet):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]

    def list(self, request):
        # client=self.request.GET['client']
        client = request.GET.get('client', None)
        print(client)
        if client is not None:
            validclient=ClientValidation(clientname=client)
            if validclient :
        # print(self.request.GET['location'])
        # print(self.request.GET['user_id'])
        # print(response)
                # print("*********List***********")
                # print("Basename:", self.basename)
                # print("Action:", self.action)
                # print("Detail:", self.detail)
                # print("Suffix:", self.suffix)
                # print("Name:", self.name)
                # print("Description:", self.description)
                res=fnClientDataCapture(Capture_id=0,client_name=client,action=self.action,client_system_name='',session_id='',method_name=self.basename
                        ,status_code='',response_message='',row_count=0,) 
                print(res)
                stu = Employee.objects.all()
                print(stu)
                Capture_id=res.get('Capture_id')
                if Capture_id>0:
                    fnClientDataCapture(Capture_id,client_name=client,action=self.action,client_system_name='',session_id='',method_name=self.basename
                        ,status_code=res.get('raise_for_status'),response_message='',row_count=stu.count()) 
                # print(stu.count())
                serializer = EmployeeSerializer(stu, many=True)
                return Response(serializer.data)
            else :
                return Response({'msg': f'{client} is not a valid client'})
        else :
                return Response({'msg': f'Provide a valid client in query string parameter'})

    def retrieve(self, request, pk=None):

        id = pk
        if id is not None:
            stu = Employee.objects.get(e_id=id)
            serializer = EmployeeSerializer(stu)
            return Response(serializer.data)

    def create(self, request):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():            
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):

        e_id = pk
        stu = Employee.objects.get(pk=e_id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk):

        id = pk
        stu = Employee.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
