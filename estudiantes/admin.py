from django.contrib import admin
from estudiantes.models import Estudiante, EstudianteAdmin, Curso,CursoAdmin
# Register your models here.

admin.site.register(Estudiante, EstudianteAdmin)

admin.site.register(Curso,CursoAdmin)
