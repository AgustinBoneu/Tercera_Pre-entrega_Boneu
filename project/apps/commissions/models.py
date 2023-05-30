from django.db import models

# Create your models here.
CURRENCY_CHOICES = [('$', 'PESOS'),('US$', 'DÓLARES'),('%', 'PORCENTAJE')]


class Identification_Commissions_Bank_USF(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Input_CommissionsBank_USF(models.Model): 
    id_commission= models.IntegerField(primary_key=True)
    name_employee = models.CharField(max_length=50)
    date = models.DateField()
    type = models.CharField(max_length=50, choices= CURRENCY_CHOICES, default='PESOS')
    amount = models.FloatField(null = True)

    def __str__(self):
        return self.name_employee

class Discount_CommissionsBank_USF(models.Model): 
    id_commission_discount =models.IntegerField(primary_key=True)
    name_client = models.CharField(max_length=50)
    percent_discount = models.IntegerField()
    def __str__(self):
        return self.name_client








    



