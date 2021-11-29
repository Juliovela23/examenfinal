from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CursoForm, EstudianteForm
from estudiantes.models import Asignacion, Estudiante, Curso
from django.utils import timezone

def curso_nuevo(request):
    if request.method == 'POST':
        formulario= CursoForm(request.POST)
        if formulario.is_valid():
            curso= Curso.objects.create(nombrecurso=formulario.cleaned_data['nombrecurso'], anio_escolar = formulario.cleaned_data['anio_escolar'],descripcion = formulario.cleaned_data['descripcion'],grado = formulario.cleaned_data['grado'])
            for estudiantes_id in request.POST.getlist('estudiantes'):
                asignacion = Asignacion(estudiante_id=estudiantes_id, curso_id=curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'asignacion creada con exito')
    else:
        formulario = CursoForm()
    return render(request, 'Estudiantes/curso_nuevo.html',{'formulario': formulario})

def estudiante_nuevo(request):
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('curso_nuevo')
    else:
        formulario = EstudianteForm()
    return render(request, 'Estudiantes/estudiante_nuevo.html', {'form': formulario})

def list_estudiantes(request):
    estudiantes = Estudiante.objects.filter(fecha_inscripcion=timezone.now()).order_by('fecha_inscripcion')
    return render(request, 'Estudiantes/index.html', {'estudiantes': estudiantes})

def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Estudiantes/cursoslist.html', {'cursos': cursos})