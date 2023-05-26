from django.shortcuts import render
from .models import Commissions_OthersBanks


# Create your views here.
def index(request):
    othersbanks = Commissions_OthersBanks.objects.all()
    datos = {"othersbanks" : othersbanks} 
    return render(request, 'othersbanks/index_othersbanks.html',datos)

