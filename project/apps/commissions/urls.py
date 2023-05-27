from django.contrib import admin
from django.urls import path
from .views import index_1,index_2,index_3

app_name = 'commissions'

urlpatterns = [
    path("index_1/", index_1, name='index_1'),
    path("index_2/", index_2, name='index_2'),
    path("index_3/", index_3, name='index_3'),
]