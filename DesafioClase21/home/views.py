from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import PersonaFormulario, BusquedaPersonaFormulario
from home.models import Persona

# Create your views here.
def crear_persona(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            # v1
            fecha_creacion = data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion = datetime.now()
            
            # v2
            # fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()
            
            return redirect('ver_personas')
    
    formulario = PersonaFormulario()
    
    return render(request, 'home/crear_persona.html', {'formulario': formulario})


def ver_personas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BusquedaPersonaFormulario()
    
    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario})

def index(request):
    
    return render(request, 'home/index.html')
