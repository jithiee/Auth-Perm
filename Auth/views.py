from django.shortcuts import render
from .serializer import StudentSerializers
from rest_framework import viewsets
from . models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.

class StudentModelApiview(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] 
    # permission_classes = [AllowAny] # all are can access this api ===== autherised and unautherised user can access
    # permission_classes = [IsAdminUser]  # only sueradmin access this apis
    
    