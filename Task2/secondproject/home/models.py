from django.db import models

# Create your models here.
class contact (models.Model):
    mobile =models.CharField(max_length=100)
    landline=models.CharField(max_length=100)
class student (models.Model):
    name =models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    course=models.CharField(max_length=100)