# Create your views here.
from django.shortcuts import render
from .ClientDataTrackingModels import ClientDataCapture
from .ClientDataTrackingSerializers import ClientDataCaptureSerializer
from rest_framework import viewsets


class ClientDataCaptureViewSet(viewsets.ModelViewSet):
    queryset = ClientDataCapture.objects.all()
    serializer_class = ClientDataCaptureSerializer
