from django.contrib import admin
from django.urls import path
from . import views
from .views import UserList

urlpatterns = [
    path('', views.formview),
    path('student',UserList.as_view()),
    path('student<pk>',views.RetrieveUserView.as_view())
 
]
