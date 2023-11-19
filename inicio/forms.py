from django import forms 

class BaseCañaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    mango = forms.CharField(max_length=30)
    pasa_hilos = forms.IntegerField()
    fecha_creacion = forms.DateTimeField(required=False)
    
class CrearCañaFormulario(BaseCañaFormulario):
    ...
    

    
class BaseReelsFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    capacidad_en_metros = forms.IntegerField()
    
class CrearReelsFormulario(BaseReelsFormulario):
    ...
    
class ActualizarReelsFormulario(BaseReelsFormulario):
    ...
    
class BaseSeñuelosFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    anzuelos = forms.IntegerField()
    color = forms.CharField(max_length=30)
    
class CrearSeñueloFormulario(BaseSeñuelosFormulario):
    ...
    
class ActualizarSeñueloFormulario(BaseSeñuelosFormulario):
    ...
    
