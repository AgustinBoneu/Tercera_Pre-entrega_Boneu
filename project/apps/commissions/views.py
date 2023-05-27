from django.shortcuts import render
from .models import Identification_Commissions_Bank_USF,Input_CommissionsBank_USF,Discount_CommissionsBank_USF

# Create your views here.
def index_1(request):
    commissions = Identification_Commissions_Bank_USF.objects.all()
    datos_1 = {"commissions" : commissions} 
    return render(request, 'commissions/index_commissions.html',datos_1)

def index_2(request):
    inputs = Input_CommissionsBank_USF.objects.all()
    datos_2 = {"inputs" : inputs} 
    return render(request, 'commissions/index_input.html',datos_2)

def index_3(request):
    discounts = Discount_CommissionsBank_USF.objects.all()
    datos_3 = {"discounts" : discounts} 
    return render(request, 'commissions/index_discount.html',datos_3)
