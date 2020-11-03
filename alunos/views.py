from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pos1.forms import AlunoForm, AlunoDisciplinaForm
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

    matriculas = AlunoDisciplina.objects.filter(idaluno=id)
    
    matriculas_result = []
    for m in matriculas:
        disciplina = Disciplina.objects.get(pk=m.iddisciplina)
        obj = {
            'info': m,
            'disciplina': disciplina
        }
        matriculas_result.append(obj)
    
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

    return render(request, 'aluno-form.html',  {'form': form, 'id': id, 'aluno': aluno, 'cursos': cursos, 'matriculas': matriculas_result})



def create_matricula(request, id):
    form = AlunoDisciplinaForm(request.POST or None)
    aluno = Aluno.objects.get(pk=id)
    curso = Curso.objects.get(pk=aluno.idcurso)
    cursoDisciplinas = CursoDisciplina.objects.filter(idcurso=aluno.idcurso)
    
    disciplinas = []
    for d in cursoDisciplinas:
        disciplinas.append(Disciplina.objects.get(id=d.iddisciplina))

    if request.method == 'POST':
        matricula = AlunoDisciplina(idaluno=aluno, iddisciplina=request.POST.get('idDisciplina'), semestre=request.POST.get('semestre'), situacao=request.POST.get('situacao'))
        matricula.save(force_insert=True)

        return HttpResponseRedirect('/alunos/')
    


    return render(request, 'matricula-form.html', {'form': form, 'aluno': aluno, 'curso': curso, 'disciplinas': disciplinas})


def delete_matricula(request, id):
    aluno = Aluno.objects.get(pk=id)

    if request.method == "POST":
        aluno.delete()
        return HttpResponseRedirect('/alunos/')

    return render(request, 'aluno-delete-confirm.html', {'aluno': aluno})


def update_matricula(request, id):
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


def delete_matricula(request, id):
    disciplina = AlunoDisciplina.objects.get(iddisciplina=id)

    if request.method == "POST":
        disciplina.delete()
        return HttpResponseRedirect('/alunos/')

    return render(request, 'aluno-disciplina-delete.html', {'disciplina': disciplina})
