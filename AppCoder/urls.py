from django.urls import path
from AppCoder.views import Profesores_formulario, buscar, busqueda_camada, cursos, cursos_formulario, estudiantes, estudiantes_formulario, inicio, profesores

urlpatterns = [
    path('', inicio, name='inicio '),
    path('cursos', cursos, name='cursos'),
    path('estudiantes', estudiantes, name='estudiantes'),
    path('profesores', profesores, name='profesores'),
    path('cursosFormulario', cursos_formulario, name='cursos_formulario'),
    path('estudiantesFormulario', estudiantes_formulario, name='estudiantes_formulario'),
    path('profesoresFormulario', Profesores_formulario, name='profesores_formulario'),
    path('busquedaCamada', busqueda_camada, name='busqueda_camada'),
    path('buscar', buscar, name='buscar'),
]