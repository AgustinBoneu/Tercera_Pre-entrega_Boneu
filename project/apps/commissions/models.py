from django.db import models

# Create your models here.
CURRENCY_CHOICES = [('$', 'PESOS'),('US$', 'DÓLARES'),('%', 'PORCENTAJE')]

class CommissionsBank_USF(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices= CURRENCY_CHOICES, default='PESOS')
    amount = models.FloatField(null = True) 

    def __str__(self):
        return self.name



    



