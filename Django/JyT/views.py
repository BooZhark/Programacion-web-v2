from django.shortcuts import redirect, render,HttpResponse
from .models import Producto, Usuario
from .Carrito import Carrito

def index(request):
    context = {
        "user": "",
    }
    return render(request, "pages/index.html", context)

def contacto(request):
    context = {}
    return render(request, "pages/contacto.html", context)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)


def user_add(request):
    if request.method != "POST":
        context = {
        }
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True


        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)


def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)

def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(rut=pk)

        context={
            "usuario":usuario,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)

def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        """ Genero la instancia """

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()

        context = {
            "mensaje": "Modificado con Exito",
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)
    
def tienda(request):
        #return HttpResponse("hola funciona :) ")
        productos = Producto.objects.all()
        return render(request,"pages/tienda.html" , {'productos':productos})

def agregar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def login(request):
    context = {}
    return render(request, "pages/login.html", context)

def monitores(request):
    context = {}
    return render(request, "pages/monitores.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registro.html", context)

def sbnosotros(request):
    context = {}
    return render(request, "pages/sbnosotros.html", context)

def tarjvideo(request):
    context = {}
    return render(request, "pages/tarjvideo.html", context)