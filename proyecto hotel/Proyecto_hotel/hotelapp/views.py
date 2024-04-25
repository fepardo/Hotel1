from django.shortcuts import render
from .models import Habitacion,Hotel,Pago,Reserva,Rol,Usuario
from django.contrib.auth.models import User #import modelo de datos de django
from django.shortcuts import redirect #import para redireccionar con django
from django.contrib.auth import authenticate,logout,login # importando la autenticacion 
from django.contrib.auth.decorators import login_required #controlar que sse vea el perfil solo logueado

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

    if request.user.is_authenticated:
        return redirect('Perfil')
    data={}


    if(request.method=='POST'):
        print(request.POST)
        user = authenticate(username=request.POST.get('correo-inicio'), password=request.POST.get('passinicio'))
        if user is not None:
            login(request,user)
            data['title']='Logueado'
            return redirect('Perfil')
            print('logueado')
        
        else:
            data['title']='No logueado :('

    return render (request,'InicioDeSesion.html',context)

def cerrarsesion(request):
    logout(request)

    return redirect('InicioDeSesion')



def RegUsuario(request):
    context={}
    return render (request,'RegUsuario.html',context)

def Perfil(request):
    if (request.user.is_authenticated):
        # Do something for authenticated users.
        context= {}
        context['user']= request.user
        perfil=Usuario.objects.get(djuser=request.user)
        context['perfil']=perfil
        return render (request,'Perfil.html',context)
    else:
        return redirect('iniciosesion')



    

def ListaUsuarios(request):
    context={}
    return render (request,'ListaUsuarios.html',context)

def RegReservas(request):
    context={}
    return render (request,'RegReservas.html',context)

def Catalogo(request):
    context={}
    return render (request,'Catalogo.html',context)
