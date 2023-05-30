from django.contrib import admin
from django.urls import path
from .views import index_1,index_2,index_3,create_commission,create_unique_commission,create_input,create_discount

app_name = 'commissions'

urlpatterns = [
    path("index_1/", index_1, name='index_1'),
    path("index_2/", index_2, name='index_2'),
    path("index_3/", index_3, name='index_3'),
    path("create/", create_commission, name="create commission"),
    path("create unique commission/", create_unique_commission, name="create unique commission"),
    path("create input/", create_input, name="create input"),
    path("create discount/", create_discount, name="create discount"),
] 