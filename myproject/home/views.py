from django.shortcuts import render
from .models import student
from rest_framework import generics
from .serializer import studentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from . forms import FormName
def formview(request):
    form=FormName()
    return render(request,"forms.html",{'forms':form})

class UserList(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class RetrieveUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer