from django.shortcuts import redirect, render
from django.http import HttpResponse
from AppCoder.forms import CursoForm, EstudianteForm, ProfesorForm

from AppCoder.models import Curso, Estudiante, Profesor


# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html',
    {'cursos': Curso.objects.all()} )

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def cursos_formulario(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            Curso.objects.create(nombre=data['curso'], camada=data['camada'])
            return redirect('cursos')
    else:
        formulario = CursoForm()
    return render(request, 'AppCoder/cursosFormulario.html ', {'formulario': formulario})

def estudiantes_formulario(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            Estudiante.objects.create(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            return redirect('estudiantes')
    else:
        formulario = EstudianteForm()
    return render(request, 'AppCoder/estudiantesFormulario.html ', {'formulario': formulario})

def Profesores_formulario(request):
    if request.method == "POST":
        formulario = ProfesorForm(request.POST)

        if formulario.is_valid(): 
            data = formulario.cleaned_data
            Profesor.objects.create(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            return redirect('profesores')
    else:
        formulario = ProfesorForm()
    return render(request, 'AppCoder/profesoresFormulario.html ', {'formulario': formulario})

def busqueda_camada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    camada = request.GET["camada"]

    if camada:
        cursos = Curso.objects.filter(camada=camada)

        return render(request, 'AppCoder/buscar.html', {'cursos': cursos, 'camada': camada})
    else:
        return HttpResponse('No se envio una camada')