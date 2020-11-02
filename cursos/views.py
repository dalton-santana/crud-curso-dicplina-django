from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pos1.forms import CursoForm
from .models import Curso, CursoDisciplina
from disciplinas.models import Disciplina


def list_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})


def create_curso(request):
    form = CursoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/cursos/')

    return render(request, 'curso-form.html', {'form': form})


def delete_curso(request, id):
    curso = Curso.objects.get(pk=id)

    if request.method == "POST":
        curso.delete()
        return HttpResponseRedirect('/cursos/')

    return render(request, 'curso-delete-confirm.html', {'curso': curso})


def update_curso(request, id):
    curso = Curso.objects.get(pk=id)
    cursoDisciplinas = CursoDisciplina.objects.filter(idcurso=curso.id)

    disciplinas = []
    for d in cursoDisciplinas:
        disciplinas.append(Disciplina.objects.get(id=d.iddisciplina))

    print(disciplinas)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cursos/')

    else:
        form = CursoForm(instance=curso)

    return render(request, 'curso-form.html',  {'form': form, 'id': id, 'curso': curso, 'disciplinas': disciplinas})


def delete_curso_discplina(request, id):
    disciplina = CursoDisciplina.objects.get(iddisciplina=id)

    if request.method == "POST":
        disciplina.delete()
        return HttpResponseRedirect('/cursos/')

    return render(request, 'curso-disciplina-delete.html', {'disciplina': disciplina})
