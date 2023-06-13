from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from core.models import faculdade
from .forms import TaskForm

def get(request):
    alunos = faculdade.objects.all()
    return render(request, 'list.html', {'alunos': alunos})


def post(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, "Aluno registrado com sucesso!")
            return redirect("/")
        else:
            messages.error(request, "Error: {}".format(form.errors))
    else:
        form = TaskForm()
       
        
    return render(request, 'form.html', {'form': TaskForm()})
