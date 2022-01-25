from django.http import HttpResponse
from django.template import Template, loader
from django.template.context import Context

# def inicio(request):
#     return HttpResponse("Bienvenido al blog de los cursos")

# def cursos(request):
#     return HttpResponse("Estos son los cursos que encontraras")

# def inicio_template(request):
#     template = loader.get_template('inicio.html')
#     contexto = Context()
#     documento = template.render(contexto)
#     return HttpResponse(documento)