import re
from urllib import request
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import FarmSerializer, FarmTypeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Farm, FarmType
# Create your views here.

class FarmListCreate(generics.ListCreateAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Farm.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)

class FarmTypeList(generics.ListAPIView):
    serializer_class = FarmTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FarmType.objects.all()

class FarmDelete(generics.DestroyAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(owner=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [AllowAny]