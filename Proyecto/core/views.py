from django.shortcuts import redirect, render
from . import forms, models

#login logout y register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def about(request):
    return render(request, 'core/about.html')

def login_view(request):
    form = AuthenticationForm(request, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña no válidos. Inténtalo de nuevo.')
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    username = request.user.username  # Obtener el nombre de usuario antes de cerrar sesión
    logout(request)
    messages.success(request, f'¡Hasta luego, {username}! Has cerrado sesión exitosamente.')
    return redirect('index')  

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')  # Cambia 'login' al nombre de tu vista de inicio de sesión
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {'form': form})


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