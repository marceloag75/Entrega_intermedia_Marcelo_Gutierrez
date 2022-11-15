from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    disciplina = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
   

class Jugador(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    categoria = models.CharField(max_length=50)
    email = models.EmailField()

class Manager(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)


