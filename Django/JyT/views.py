from django.shortcuts import redirect, render, HttpResponse
from .models import Producto, Usuario
from .Carrito import Carrito
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def index(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            usuario_autenticado = Usuario.objects.get(pk=user_id)
            nombre_usuario = usuario_autenticado.nombre
            return render(request, 'pages/index.html', {'nombre_usuario': nombre_usuario})
        except Usuario.DoesNotExist:
            pass
    
    return render(request, 'pages/index.html')

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

def registro(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        password = request.POST.get('password')

        nuevo_usuario = Usuario(rut=rut, nombre=nombre, apellido_paterno=apellido_paterno,
                                apellido_materno=apellido_materno, email=email, telefono=telefono,
                                direccion=direccion, password=password, activo=True)
        nuevo_usuario.save()

        return redirect('index')

    context = {}
    return render(request, 'pages/registro.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            user = None
        
        if user and check_password(password, user.password):
            request.session['user_id'] = user.pk 
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            return render(request, 'pages/login.html')
    else:
        return render(request, 'pages/login.html')
    
def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']

    return redirect('index') 