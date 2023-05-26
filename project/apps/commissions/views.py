from django.shortcuts import render
from .models import CommissionsBank_USF

# Create your views here.
def index(request):
    commissions = CommissionsBank_USF.objects.all()
    datos = {"commissions" : commissions} 
    return render(request, 'commissions/index_commissions.html',datos)
