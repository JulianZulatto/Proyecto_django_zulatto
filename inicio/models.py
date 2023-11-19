from django.db import models

class CañaDePescar(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    mango = models.TextField()
    pasa_hilos = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo}'

class Reels(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    capacidad_en_metros = models.TextField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.capacidad_en_metros}'
    
class Señuelo(models.Model):
    modelo = models.CharField(max_length=30)
    anzuelos = models.IntegerField()
    color = models.TextField()
    
    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.color} - {self.anzuelos}'
    

