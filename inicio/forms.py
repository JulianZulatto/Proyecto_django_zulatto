from django import forms 

class CrearCañaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    mango = forms.CharField(max_length=30)
    pasa_hilos = forms.IntegerField()
    
    
class CrearReelsFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    capacidad_en_metros = forms.IntegerField()
    
class CrearSeñuelosFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    anzuelos = forms.IntegerField()
    color = forms.CharField(max_length=30)