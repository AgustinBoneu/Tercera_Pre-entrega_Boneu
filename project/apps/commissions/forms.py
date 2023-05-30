from django import forms
from . import models

CURRENCY_CHOICES = [('$', 'PESOS'),('US$', 'DÓLARES')]

class Identification_Commissions_Bank_USFForm(forms.ModelForm):
    class Meta:
        model = models.Identification_Commissions_Bank_USF
        fields = '__all__'

class Input_CommissionsBank_USFForm(forms.ModelForm):
    class Meta:
        model = models.Input_CommissionsBank_USF
        fields = '__all__'

class Discount_CommissionsBank_USFForm(forms.ModelForm):
    class Meta:
        model = models.Discount_CommissionsBank_USF
        fields = '__all__'