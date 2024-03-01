from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('about',views.add),
    path('insert',views.insert),
    path('delete/<id>',views.delete),
    path('edit/<id>',views.edit),
    path('update/<id>',views.update),
    ]
