from django.shortcuts import render, redirect

from inicio.models import CañaDePescar, Reels, Señuelo
from inicio.forms import CrearCañaFormulario, BaseReelsFormulario,BaseSeñuelosFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


def inicio(request):
    return render(request, 'base.html', {})

@login_required
def caña_de_pescar(request):
    
    marca_a_buscar = request.GET.get('marca')
    
    if marca_a_buscar:
        listado_de_cañas = CañaDePescar.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_cañas = CañaDePescar.objects.all()
        
    return render(request, 'cañas.html', {'listado_de_cañas': listado_de_cañas})

@login_required
def crear_caña(request):
    if request.method == 'POST':
        formulario = CrearCañaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            mango = info_limpia.get('mango')
            pasa_hilos = info_limpia.get('pasa_hilos')
            fecha_creacion = info_limpia.get('fecha_creacion')
            
            
            
            caña_de_pescar = CañaDePescar(marca = marca.lower(), modelo = modelo, mango = mango, pasa_hilos= pasa_hilos, fecha_creacion = fecha_creacion)
            caña_de_pescar.save()
            
            return redirect('cañas') 
        else:
            return render(request, 'crear_caña.html', {'formulario': formulario})
    
    formulario = CrearCañaFormulario()
    return render(request, 'crear_caña.html', {'formulario': formulario})

class ActualizarCaña(LoginRequiredMixin, UpdateView):
    model = CañaDePescar
    template_name = 'actualizar_caña.html'
    fields = ['marca', 'modelo', 'mango','pasa_hilos', 'fecha_creacion']
    success_url = reverse_lazy('cañas')
    
class DetalleCaña(DetailView):
    model = CañaDePescar
    template_name = 'detalle_caña.html'
    
class EliminarCaña(LoginRequiredMixin, DeleteView):
    model = CañaDePescar
    template_name = 'eliminar_caña.html'
    success_url = reverse_lazy('cañas')
    



def reels(request):
    
    marca_a_buscar = request.GET.get('marca')
    
    if marca_a_buscar:
        listado_de_reels = Reels.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_reels = Reels.objects.all()
        
    return render(request, 'reels.html', {'listado_de_reels': listado_de_reels})


def crear_reels(request):
    if request.method == 'POST':
        formulario = BaseReelsFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            capacidad_en_metros = info_limpia.get('capacidad_en_metros')
            
            
            reel = Reels(marca = marca.lower(), modelo = modelo, capacidad_en_metros = capacidad_en_metros)
            reel.save()
            
            return redirect('reels') 
        else:
            return render(request, 'crear_reels.html', {'formulario': formulario})
    
    formulario = BaseReelsFormulario()
    return render(request, 'crear_reels.html', {'formulario': formulario})

def señuelo(request):
    
    modelo_a_buscar = request.GET.get('modelo')
    
    if modelo_a_buscar:
        listado_de_señuelos = Señuelo.objects.filter(modelo__icontains=modelo_a_buscar)
    else:
        listado_de_señuelos = Señuelo.objects.all()
        
    return render(request, 'señuelo.html', {'listado_de_señuelos': listado_de_señuelos})

def crear_señuelo(request):
    if request.method == 'POST':
        formulario = BaseSeñuelosFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            modelo = info_limpia.get('modelo')
            anzuelos = info_limpia.get('anzuelos')
            color = info_limpia.get('color')
            
            
            señuelo = Señuelo(modelo = modelo.lower(), anzuelos = anzuelos, color = color)
            señuelo.save()
            
            return redirect('señuelos') 
        else:
            return render(request, 'crear_señuelo.html', {'formulario': formulario})
    
    formulario = BaseSeñuelosFormulario()
    return render(request, 'crear_señuelo.html', {'formulario': formulario})

