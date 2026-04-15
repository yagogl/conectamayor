from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario, GrupoFamiliar
from .forms import RegistroForm


def inicio(request):
    """Redirige al login o a la pantalla correcta según el rol."""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.es_mayor:
        return redirect('inicio_mayor')
    return redirect('inicio_familiar')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registro(request):
    """Registro de nuevo usuario. El familiar-editor crea el grupo familiar."""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            rol = form.cleaned_data['rol']
            user.rol = rol

            if rol == 'editor':
                # El editor crea un grupo familiar nuevo
                nombre_grupo = form.cleaned_data.get('nombre_grupo', '')
                grupo = GrupoFamiliar.objects.create(nombre=nombre_grupo)
                user.grupo_familiar = grupo

            user.save()

            # Si no es editor, puede unirse con código después
            login(request, user)

            if rol == 'editor':
                messages.success(
                    request,
                    f'Grupo familiar creado. Tu código es: {grupo.codigo}'
                )
            else:
                messages.info(
                    request,
                    'Cuenta creada. Únete a un grupo familiar con el código que te han compartido.'
                )
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def unirse_grupo(request):
    """Permite a un usuario sin grupo unirse con un código."""
    if request.user.grupo_familiar:
        messages.info(request, 'Ya perteneces a un grupo familiar.')
        return redirect('inicio')

    if request.method == 'POST':
        codigo = request.POST.get('codigo', '').strip().upper()
        try:
            grupo = GrupoFamiliar.objects.get(codigo=codigo)
            request.user.grupo_familiar = grupo
            request.user.save()
            messages.success(request, f'Te has unido al grupo {grupo.nombre or codigo}.')
            return redirect('inicio')
        except GrupoFamiliar.DoesNotExist:
            messages.error(request, 'Código incorrecto. Comprueba que lo has escrito bien.')

    return render(request, 'usuarios/unirse_grupo.html')


@login_required
def inicio_mayor(request):
    if not request.user.es_mayor:
        return redirect('inicio_familiar')
    return render(request, 'usuarios/mayor/inicio.html')


@login_required
def inicio_familiar(request):
    if request.user.es_mayor:
        return redirect('inicio_mayor')
    return render(request, 'usuarios/familiar/inicio.html')
