from django.conf.urls import url
from . import  views

urlpatterns = [
    url('Curso/nuevo/', views.curso_nuevo, name='curso_nuevo'),
    url('Estudiante/nuevo/', views.estudiante_nuevo, name='estudiante_nuevo'),
    url('Estudiantes/', views.list_estudiantes, name='list_estudiantes'),
    url('curso/',views.list_cursos, name='list_cursos'),
]
