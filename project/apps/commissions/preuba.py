
from django import forms
class Perro (forms.ModelForm):
    def __init__(self,name):
        self.name = name 

p1  = ("Fido")