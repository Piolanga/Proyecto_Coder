from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', inicio),
    path('cursos', cursos),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
]