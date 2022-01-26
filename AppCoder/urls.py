from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', inicio, name='inicio '),
    path('cursos', cursos, name='cursos'),
    path('estudiantes', estudiantes, name='estudiantes'),
    path('profesores', profesores, name='profesores'),
]