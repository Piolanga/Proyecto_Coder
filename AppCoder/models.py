from django.db import models
from django.db.models import Model
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Curso(Model):
    asignatura = CharField(max_length=30)
    seccion = IntegerField()

class Estudiante(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()

class Profesor(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)