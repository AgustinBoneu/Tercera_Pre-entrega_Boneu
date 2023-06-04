from django.shortcuts import render,redirect
from .models import Identification_Commissions_Bank_USF,Input_CommissionsBank_USF,Discount_CommissionsBank_USF
from . import forms

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

def create_commission(request):  
    if request.method == "POST":
        form1 = forms.Identification_Commissions_Bank_USFForm(request.POST)
        form2 = forms.Input_CommissionsBank_USFForm(request.POST)
        form3 = forms.Discount_CommissionsBank_USFForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect("index")
    else: 
        form1 = forms.Identification_Commissions_Bank_USFForm()
        form2 = forms.Input_CommissionsBank_USFForm()
        form3 = forms.Discount_CommissionsBank_USFForm()
        context = {"form1": form1, "form2": form2, "form3": form3}
    return render (request,"commissions/create.html",context)

def create_commission(request):  
    if request.method == "POST":
        form1 = forms.Identification_Commissions_Bank_USFForm(request.POST)
        form2 = forms.Input_CommissionsBank_USFForm(request.POST)
        form3 = forms.Discount_CommissionsBank_USFForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect("index")
    else: 
        form1 = forms.Identification_Commissions_Bank_USFForm()
        form2 = forms.Input_CommissionsBank_USFForm()
        form3 = forms.Discount_CommissionsBank_USFForm()
        context = {"form1": form1, "form2": form2, "form3": form3}
    return render (request,"commissions/create.html",context)

def create_unique_commission(request): 
    form = forms.Identification_Commissions_Bank_USFForm(request.POST) 
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    context = {"form": form}
    return render (request,"commissions/create_unique.html",context)

def create_input(request): 
    form = forms.Input_CommissionsBank_USFForm(request.POST) 
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    context = {"form": form}
    return render (request,"commissions/create_input.html",context)

def create_discount(request):  
    form = forms.Discount_CommissionsBank_USFForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")
    context = {"form": form}
    return render (request,"commissions/create_discount.html",context)

