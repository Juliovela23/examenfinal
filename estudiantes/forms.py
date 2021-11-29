from django import forms
from django.db.models import fields
from .models import Estudiante, Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields = ('nombrecurso','descripcion','anio_escolar','grado','estudiantes')
    
    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["estudiantes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["estudiantes"].help_text = "Ingrese el estudiante correspondiente al curso"
        self.fields["estudiantes"].queryset = Estudiante.objects.all()

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ( 'nombre','apellidos' ,'fecha_nacimiento','fecha_inscripcion' ,'carnet',)
        
        