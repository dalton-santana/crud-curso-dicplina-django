from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pos1.forms import DisciplinaForm, CursoDisciplinaForm
from .models import Disciplina
from cursos.models import Curso, CursoDisciplina


def list_disciplinas(request):
	disciplinas = Disciplina.objects.all()
	return render(request, 'disciplinas.html', {'disciplinas': disciplinas})


def create_disciplina(request):
	form = DisciplinaForm(request.POST or None)
	cursos = Curso.objects.all()

	print(request.POST)
	
	if request.method == 'POST' and form.is_valid():
		disciplina = form.save()

		curso = Curso.objects.get(pk=request.POST.get('curso_id'))
		disciplina = Disciplina.objects.get(pk=disciplina.id)

		formCursoDisciplina = CursoDisciplina(idcurso=curso, iddisciplina=disciplina.id)
		formCursoDisciplina.save(force_insert=True)
		
		return HttpResponseRedirect('/disciplinas/')

	return render(request,'disciplina-form.html', {'form': form, 'cursos': cursos})


def delete_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)

    if request.method == "POST":
        disciplina.delete()
        return HttpResponseRedirect('/disciplinas/')

    return render(request, 'disciplina-delete-confirm.html', {'disciplina': disciplina})


def update_disciplina(request, id):
	disciplina = Disciplina.objects.get(pk=id)
	
	if request.method == 'POST':
		form = DisciplinaForm(request.POST, instance=disciplina)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/disciplinas/')

	else:
		form = DisciplinaForm(instance=disciplina)
		
	return render(request, 'disciplina-form.html',  {'form': form, 'id': id, 'disciplina': disciplina})	
