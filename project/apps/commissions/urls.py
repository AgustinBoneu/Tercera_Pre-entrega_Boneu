from django.contrib import admin
from django.urls import path
from .views import index

app_name = 'commissions'

urlpatterns = [
    path("", index, name='index'),
]