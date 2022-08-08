from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pqrs import models
from django.contrib import auth
from pqrs.models import *
import threading
from django.core.mail import send_mail
import random
from django.contrib.auth import get_user_model

# Create your views here.
def Principal(request):
    oficinas =  get_user_model().objects.all()
    username = request.POST.get('txtUsuario', None)
    password = request.POST.get('txtContraseña', None)

    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        if user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/')
    else:
       a = messages.success(request, "Registro exitoso")
       data={
           'a':a,
           'oficinas':oficinas,
       }
    return render(request, "principal.html",data)


def SubirPqrs(request):
    numero = 18210012
    oficinas = Oficina.objects.all()
    
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        correo = request.POST.get("correo")
        oficina = Oficina.objects.get(id = request.POST['oficina'])
        barrio = request.POST.get("barrio")
        archivo = request.FILES.get("archivo")
        codigo = format(id(numero), 'x')
        pqr = Pqr(titulo=titulo,correo=correo, oficina=oficina, barrio=barrio, archivo=archivo, codigo=codigo)
        # Saving the information in the database
        pqr.save()
        email_desde = settings.EMAIL_HOST_USER
        email_para = [correo]
        asunto = 'Su PQR se ha registrado correcta mente'
        mensaje =f'Su codigo de PQR es {codigo}'
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, "Registro exitoso su codigo es  " + codigo)
    return render(request, "subirPqrs.html",{'oficinas':oficinas})


def tablapqr(request, codigo):
    codi = codigo
    fil = Pqr.objects.filter(codigo = codi)
    data={
        'fil':fil,  
    }
    return render(request, "ConsultarPqr.html",data)


def obtenerPqrs(request):
    pqrs= Pqr.objects.all()
    data={
        'pqrs':pqrs
    }
    return render(request, "panelControl.html", data)

def Oficinas(request):
    oficinas =  get_user_model().objects.all()
    data={
        'oficinas':oficinas
    }
    return render(request, "oficinas.html", data)

