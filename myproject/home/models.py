from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response

class student(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
