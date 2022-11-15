from django.shortcuts import render

from .models import Equipo, Jugador, Manager
from .forms import form_escuela, inscripcion_alumnos, form_entrenador 
# Create your views here.


def mostrar_index(request):

    return render(request,'AppFamilia/index.html')

def escuela(request):
    if request.method == 'POST':

        formulario = form_escuela(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

        escuela = Equipo(disciplina=formulario_limpio['disciplina'], categoria=formulario_limpio['categoria'])
        escuela.save()
        return render(request, 'AppFamilia/index.html')

    else:
        formulario = form_escuela()
    return render(request, 'AppFamilia/escuela.html', {'formulario': formulario})
 


def alumnos(request):
    if request.method == 'POST':

        formulario = inscripcion_alumnos(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

        alumno = Jugador(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], categoria=formulario_limpio['categoria'], email=formulario_limpio['email'])
        alumno.save()
        return render(request, 'AppFamilia/index.html')

    else:
        formulario = inscripcion_alumnos()
    return render(request, 'AppFamilia/alumnos.html', {'formulario': formulario})
 
  
def entrenador(request):

    if request.method == 'POST':

        formulario = form_entrenador(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            entrenador= Manager(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], profesion=formulario_limpio['profesion'], email=formulario_limpio['email'])
            entrenador.save()
            return render(request, 'AppFamilia/index.html')

    else:
        formulario = form_entrenador()
    return render(request, 'AppFamilia/entrenador.html', {'formulario': formulario})


def buscar_disciplina(request):

    data = request.GET.get('disciplina', "")
    error = ""
    if data:
        try:
            equipo = Equipo.objects.get(disciplina=data) 
            return render (request, 'Appfamilia/buscar_disciplina.html', {'equipo':equipo, 'disciplina': data})
        except Exception as exc:
            error = 'no existe'

    return render (request, 'Appfamilia/buscar_disciplina.html', {'error':error})

      #  disciplina = request.GET['disciplina']
      # disciplinas = Equipo.objects.filter(disciplina__icontains=disciplina)

      # return render (request, 'Appfamilia/buscar_disciplina.html', {'disciplinas':disciplinas})

    #else: 
      #   respuesta = 'No hay disciplina disponible'
    #return render (request, 'Appfamilia/buscar_disciplina.html', {'respuesta':respuesta})

