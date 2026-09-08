from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import ContactForm, loginForm, resgisterForm
from django.contrib.auth import authenticate, login, get_user_model


User = get_user_model()

def home_page(request):
    contexto = {
        'title': 'Home Page',
        'content': 'Bem vindo a Pagina Principal'
    }

    if request.user.is_authenticated:
        contexto["premium_content"] = "Voce e um usuario Premium"
    return render(request, 'home_page.html', contexto)


def contact_page(request):
    form = ContactForm(request.POST or None)
    contexto = {
        'title': 'Contato Page',
        'content': 'Bem vindo a Pagina de Contato',
        'form': form
    }
    
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'contact/contact_page.html', contexto)


def about_page(request):
    form = ContactForm(request.POST)
    contexto = {
        'title': 'About Page',
        'content': 'Bem vindo a Pagina de about',
        'form': form
    }
    return render(request, 'about/about_page.html', contexto)


def login_page(request):
    formLogin = loginForm(request.POST or None)
    contexto = {
        'formLogin': formLogin
    }

    if formLogin.is_valid():
        username = formLogin.cleaned_data.get('username')
        password = formLogin.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print("Login Valido")
            return redirect('/')

        else:
            print("Login Invalido")
    
    return render(request, 'auth/login_page.html', contexto)


def register_page(request):
    formRegister = resgisterForm(request.POST or None)
    contexto = {
        'formRegister': formRegister
    }

    if formRegister.is_valid():
        username = formRegister.cleaned_data.get('username')
        email = formRegister.cleaned_data.get('email')
        password = formRegister.cleaned_data.get('password')
        new_user = User.objects.create_user(username=username,email=email,password=password)
        print(new_user)

    return render (request, 'auth/register_page.html', contexto)