from django.db import models
from django.contrib import admin
# Modelo estudiantes

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_inscripcion = models.DateField()
    carnet= models.CharField(max_length=100)
    def __str__(self):
         return self.nombre + ' ' +self.apellidos
     

class Curso(models.Model):
    nombrecurso = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    anio_escolar = models.IntegerField()
    grado = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Estudiante, through='Asignacion')
    
    def __str__(self):
        return self.nombrecurso
    
        
class Asignacion(models.Model):
    estudiante =models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class AsignacionLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class EstudianteAdmin(admin.ModelAdmin):
    inlines=(AsignacionLine,)

class CursoAdmin(admin.ModelAdmin):
    inlines=(AsignacionLine,)
