from code import interact
from msilib.schema import Class
from django.forms import EmailField, Form, CharField, IntegerField 

class CursoForm(Form):
    curso = CharField()
    camada = IntegerField()

class EstudianteForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()

class ProfesorForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    profesion = CharField()