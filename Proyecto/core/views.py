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

def cliente_list(request):
    consulta = models.Cliente.objects.all()
    contexto = {"cliente": consulta}
    return render(request, "core/cliente_list.html", contexto)

def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = forms.ClienteForm()
    return render(request, "core/cliente_create.html", {"form": form})

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
