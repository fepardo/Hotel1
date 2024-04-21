from django.shortcuts import render
from .models import Habitacion,Hotel,Pago,Reserva,Rol,Usuario

# Create your views here.
def index(request):
    context={
        'hoteles': Hotel.objects.all()
    }
    return render (request,'index.html',context)



def pagina2(request):
    context={}
    return render (request,'2.html',context)


def InicioDeSesion(request):
    context={}
    return render (request,'InicioDeSesion.html',context)

def RegUsuario(request):
    context={}
    return render (request,'RegUsuario.html',context)

def Perfil(request):
    context={}
    return render (request,'Perfil.html',context)

def ListaUsuarios(request):
    context={}
    return render (request,'ListaUsuarios.html',context)

def RegReservas(request):
    context={}
    return render (request,'RegReservas.html',context)

def Catalogo(request):
    context={}
    return render (request,'Catalogo.html',context)
