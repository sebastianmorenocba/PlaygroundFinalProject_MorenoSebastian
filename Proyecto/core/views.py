from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "core/index.html")


def mecanico_list(request):
    consulta = models.Mecanico.objects.all()
    contexto = {"mecanico": consulta}
    return render(request, "core/mecanico_list.html", contexto)


def mecanico_create(request):
    if request.method == "POST":
        form = forms.MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mecanico_list")
    else:
        form = forms.MecanicoForm()
    return render(request, "core/mecanico_create.html", {"form": form})

def estudiante_list(request):
    consulta = models.Estudiante.objects.all()
    contexto = {"estudiante": consulta}
    return render(request, "core/estudiante_list.html", contexto)

def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("estudiante_list")
    else:
        form = forms.EstudianteForm()
    return render(request, "core/estudiante_create.html", {"form": form})

def curso_list(request):
    consulta = models.Curso.objects.all()
    contexto = {"curso": consulta}
    return render(request, "core/curso_list.html", contexto)

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = forms.CursoForm()
    return render(request, "core/curso_create.html", {"form": form})
