from django.db import models

# Create your models here.
CURRENCY_CHOICES = [('$', 'PESOS'),('US$', 'DÓLARES'),('%', 'PORCENTAJE')]

class Name_Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Commissions_OthersBanks(models.Model):
    id_bank = models.ForeignKey(Name_Bank, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=CURRENCY_CHOICES, default='PESOS')
    amount = models.FloatField(null=True) or models.CharField(max_length=50)
    def __str__(self):
        return self.name
    