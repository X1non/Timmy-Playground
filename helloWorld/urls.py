from django.urls import path
from . import views

app_name = 'helloWorld'

urlpatterns = [
    path('', views.index, name='index'),
]