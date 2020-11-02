# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect


def init(request):
	return render(request, 'tela-inicial.html')

