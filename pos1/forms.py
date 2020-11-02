from django import forms
from cursos.models import Curso, CursoDisciplina
from disciplinas.models import Disciplina


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class CursoDisciplinaForm(forms.ModelForm):
    class Meta:
        model = CursoDisciplina
        fields = '__all__'