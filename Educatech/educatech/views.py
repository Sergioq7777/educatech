from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

#from django.contrib.auth.models import User
from users.models import User


from EduT.forms import RegisterForm
from .models import *
from subjects.models import *
# Create your views here.

def Index(request):

    products = Product.objects.all().order_by('-id')

    return render(request, "app2.html", {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products,

    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña no valida")


    return render(request, 'users/login.html',{


    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html',{
        'form': form

    })