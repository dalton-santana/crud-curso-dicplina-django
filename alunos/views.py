from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pos1.forms import AlunoForm
from .models import Aluno, AlunoDisciplina
from disciplinas.models import Disciplina
from cursos.models import Curso, CursoDisciplina


def list_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})


def create_aluno(request):
    form = AlunoForm(request.POST or None)
    cursos = Curso.objects.all()

    if request.method == 'POST' and form.is_valid():
        aluno = form.save()

        aluno = Aluno.objects.get(pk=aluno.id)
        aluno.idcurso = request.POST.get('idCurso')
        aluno.save()

        return HttpResponseRedirect('/alunos/')

    return render(request, 'aluno-form.html', {'form': form, 'cursos': cursos})


def delete_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)

    if request.method == "POST":
        aluno.delete()
        return HttpResponseRedirect('/alunos/')

    return render(request, 'aluno-delete-confirm.html', {'aluno': aluno})


def update_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    cursos = Curso.objects.all()

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        form.save()

        aluno.idcurso = request.POST.get('idCurso')
        aluno.save()

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/alunos/')

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'aluno-form.html',  {'form': form, 'id': id, 'aluno': aluno, 'cursos': cursos})


def delete_aluno_discplina(request, id):
    disciplina = AlunoDisciplina.objects.get(iddisciplina=id)

    if request.method == "POST":
        disciplina.delete()
        return HttpResponseRedirect('/alunos/')

    return render(request, 'aluno-disciplina-delete.html', {'disciplina': disciplina})
