from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })


@login_required(login_url='/login')
def about_us(request):

    return render(request, 'mainapp/about_us.html', {
    })


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/inicio')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                messages.success(request, 'Te has registrado Bien')

                return redirect('/inicio')

        return render(request, 'Mainapp/user/register.html', {
            'title': 'Registro',
            'register_form': register_form,
        })


def login_page(request):
    if request.user.is_authenticated:  # Redirigimos el acceso a algunas vistas si se estan
        return redirect('/inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/inicio')
            else:
                messages.warning(request, 'No Te has identificado')

        return render(request, 'Mainapp/user/login.html', {
            'title': 'Identificate'
        })


def logout_user(request):

    logout(request)

    return redirect('/login')
