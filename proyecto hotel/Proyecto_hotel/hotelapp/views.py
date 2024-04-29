from django.shortcuts import render
from .models import Habitacion,Hotel,Pago,Reserva,Rol,Usuario
from django.contrib.auth.models import User #import modelo de datos de django
from django.shortcuts import redirect #import para redireccionar con django
from django.contrib.auth import authenticate,logout,login # importando la autenticacion 
from django.contrib.auth.decorators import login_required #controlar que sse vea el perfil solo logueado
from datetime import datetime

# Create your views here.
def index(request):
    context={
        'hoteles': Hotel.objects.all()
    }
    return render (request,'index.html',context)



def pagina2(request):
    
    habitaciones = Habitacion.objects.all() # select * from
    context={
        'habitaciones' :habitaciones

    }
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
    context["usuarios"]= Usuario.objects.all()
    return render (request,'ListaUsuarios.html',context)

def RegReservas(request):
    context={}
    context["reservas"]= Reserva.objects.all()

    return render (request,'RegReservas.html',context)

def Catalogo(request):
    context={}
    return render (request,'Catalogo.html',context)


def Reservar(request, habitacion_id):
    context={}

    context["habitacion_id"]= habitacion_id
    print(habitacion_id)

    
    if(request.method=='POST'):
        print (request.POST)
        if (request.user.is_authenticated):
            usuarioActivo= Usuario.objects.get(djuser=request.user)

            print (request.POST)
            reserva = Reserva( cliente=usuarioActivo, id_habitacion= Habitacion.objects.get(habitacion_id= request.POST['habitacion_id'] ),
             fecha_inicio=request.POST['inicio'],fecha_creacion= datetime.now()  , fecha_termino= request.POST['Termino'])
            reserva.save()




    return render (request,'Reservar.html',context)
