from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pos1.forms import DisciplinaForm
from .models import Disciplina
from cursos.models import Curso


def list_disciplinas(request):
	disciplinas = Disciplina.objects.all()
	return render(request, 'disciplinas.html', {'disciplinas': disciplinas})


def create_disciplina(request):
	form = DisciplinaForm(request.POST or None)
	cursos = Curso.objects.all()
	
	if request.method == 'POST' and form.is_valid():
		form.save()
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