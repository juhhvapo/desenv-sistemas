from django.shortcuts import render
from .models import Tarefa
from django.http import HttpResponse

def listar_tarefas(request):
    Tarefas.salvas = Tarefa.objects.all()
    contexto = {
                "minhas_tarefas":tarefas_salvas
               }

    return render (request ,'tarefas/lista.httml',contexto)