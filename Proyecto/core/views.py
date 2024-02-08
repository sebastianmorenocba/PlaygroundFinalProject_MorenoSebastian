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

def vehiculo_list(request):
    consulta = models.Vehiculo.objects.all()
    contexto = {"vehiculo": consulta}
    return render(request, "core/vehiculo_list.html", contexto)

def vehiculo_create(request):
    if request.method == "POST":
        form = forms.VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vehiculo_list")
    else:
        form = forms.VehiculoForm()
    return render(request, "core/vehiculo_create.html", {"form": form})
