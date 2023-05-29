from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Entrada, Salida, Proveedores, Materiales, Clientes, Productos, Barcos, ZonasFAO, ArtesPesca
from .forms import RegistrarEntrada,RegistrarSalida
from datetime import datetime, date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from openpyxl import Workbook
@login_required
def Signup(request):
    if request.method=='GET':
        return render(request, 'Signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            #Registrar usuario
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login (request, user)
                return redirect('Signup')
            except IntegrityError:
                return render(request, 'Signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'Signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })
@login_required
def CerrarSesion(request):
    logout(request)
    return redirect('Login')
def AbrirSesion(request):
    if request.method =='GET':
        return render(request, 'login.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request, username=request.POST['username'],
        password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Nombre o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('RegistroEntradas')

def Inicio(request):
    return render(request, 'Indice.html')
def Nosotros(request):
    return render(request, 'Nosotros.html')
def Productos(request):
    return render(request, 'Productos.html')
@login_required
def exportar_a_excel(request):
    # Filtra los datos por la fecha actual
    datos = Entrada.objects.filter(fecha=date.today())

    # Crea un libro de trabajo y una hoja
    libro = Workbook()
    hoja = libro.active

    # Agrega los encabezados de las columnas
    hoja.append(['id', 'lote', 'codigo_proveedor', 'nombre_proveedor', 'codigo_especie', 'especie', 'cantidad_kg',
                 'cantidad_caja', 'precio_kg', 'precio_caja', 'fecha', 'albaran', 'codigo_zona_captura',
                 'codigo_arte_pesca', 'fecha_captura', 'codigo_barco'])

    # Agrega los datos a la hoja
    for dato in datos:
        hoja.append([dato.id, dato.lote, dato.codigo_proveedor.codigo_proveedor, dato.nombre_proveedor,
                     dato.codigo_especie.codigo_material, dato.especie, dato.cantidad_kg, dato.cantidad_caja,
                     dato.precio_kg, dato.precio_caja, dato.fecha, dato.albaran, dato.codigo_zona_captura,
                     dato.codigo_arte_pesca, dato.fecha_captura, dato.codigo_barco])

    # Crea la respuesta HTTP con el archivo de Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=datos.xlsx'
    libro.save(response)

    return response
# Vamos a crear las pantallas aqui.


@login_required
def RegistroEntradas(request):
    if request.method=="GET":
        return render (request, 'RegistroEntradas.html',{
            'form':RegistrarEntrada()
        })
    else:
        proveedor = Proveedores.objects.get(pk=request.POST['nombre_proveedor'])
        especie = Materiales.objects.get(pk=request.POST['especie'])
        barco=Barcos.objects.get(pk=request.POST['codigo_barco'])
        artepesca = ArtesPesca.objects.get(pk=request.POST['codigo_arte'])
        zona = ZonasFAO.objects.get(pk=request.POST['codigo_zona'])
        # Obtener la fecha actual en el formato deseado
        fecha = datetime.now().strftime('%d%m%Y')

        # Crear el lote concatenando la fecha y el código de proveedor
        lote = fecha + '-' + str(proveedor.codigo_proveedor).zfill(6)
        Entrada.objects.create(
            codigo_proveedor=proveedor,  # asigna el objeto completo del proveedor
            nombre_proveedor=proveedor.nombre_proveedor,  # asigna el nombre del proveedor
            codigo_especie=especie,
            especie=especie.nombre_material,
            cantidad_kg=request.POST['cantidad_kg'],
            cantidad_caja=request.POST['cantidad_caja'],
            precio_kg=request.POST['precio_kg'],
            precio_caja=request.POST['precio_caja'],
            lote=lote,
            codigo_zona=zona,
            codigo_arte=artepesca,
            codigo_barco=barco,
        )
        return render(request, 'RegistroEntradas.html', {
            'form': RegistrarEntrada()
        })
@login_required
def EliminarEntrada(request, id_entrada):
    entrada = get_object_or_404(Entrada, id=id_entrada)
    entrada.delete()
    return redirect('Entradas')
@login_required
def EditarEntrada(request, id_entrada):
    entrada = Entrada.objects.get(pk=id_entrada)
    if request.method == 'POST':
        form = RegistrarEntrada(request.POST)
        if form.is_valid():
            entrada.nombre_proveedor_id = form.cleaned_data['nombre_proveedor']
            entrada.especie = form.cleaned_data['especie'].nombre_material
            entrada.cantidad_kg = form.cleaned_data['cantidad_kg']
            entrada.cantidad_caja = form.cleaned_data['cantidad_caja']
            entrada.precio_kg = form.cleaned_data['precio_kg']
            entrada.precio_caja = form.cleaned_data['precio_caja']
            entrada.codigo_zona = form.cleaned_data['codigo_zona']
            entrada.codigo_arte = form.cleaned_data['codigo_arte']
            entrada.codigo_barco = form.cleaned_data['codigo_barco']
            entrada.save()
            return redirect('Entradas')
    else:
        form = RegistrarEntrada(initial={
            'nombre_proveedor': entrada.nombre_proveedor,
            'especie': entrada.especie,
            'cantidad_kg': entrada.cantidad_kg,
            'cantidad_caja': entrada.cantidad_caja,
            'precio_kg': entrada.precio_kg,
            'precio_caja': entrada.precio_caja,
            'codigo_zona': entrada.codigo_zona,
            'codigo_arte': entrada.codigo_arte,
            'codigo_barco': entrada.codigo_barco,
        })
    return render(request, 'RegistroEntradas.html', {'form': form, 'id_entrada': id_entrada})

@login_required
def RegistroSalidas(request):
    if request.method == 'GET':
        return render(request,'RegistroSalidas.html',{
            'form': RegistrarSalida
    })
    else:
        cliente = Clientes.objects.get(pk=request.POST['nombre_cliente'])
        especie = Productos.objects.get(pk=request.POST['especie'])
        salida=Salida.objects.create(
            codigo_cliente_id=cliente,  # asigna el objeto completo del proveedor
            nombre_cliente=cliente.nombre_cliente,
            codigo_especie_id=especie,
            especie=especie.nombre_producto,
            cantidad_kg=request.POST['cantidad_kg'],
            cantidad_caja=request.POST['cantidad_caja'],
            precio_kg=request.POST['precio_kg'],
            precio_caja=request.POST['precio_caja'])
        return render(request,'RegistroSalidas.html',{
        'form': RegistrarSalida()
    })
@login_required
def EliminarSalida(request, id_salida):
    salida = get_object_or_404(Salida, id=id_salida)
    salida.delete()
    return redirect('Salidas')
@login_required
def EditarSalida(request, id_salida):
    salida = Salida.objects.get(pk=id_salida)
    if request.method == 'POST':
        form = RegistrarSalida(request.POST)
        if form.is_valid():
            salida.nombre_cliente = form.cleaned_data['nombre_cliente'].nombre_cliente
            salida.especie = form.cleaned_data['especie'].nombre_producto
            salida.cantidad_kg = form.cleaned_data['cantidad_kg']
            salida.cantidad_caja = form.cleaned_data['cantidad_caja']
            salida.precio_kg = form.cleaned_data['precio_kg']
            salida.precio_caja = form.cleaned_data['precio_caja']
            salida.save()
            return redirect('Salidas')
    else:
        form = RegistrarSalida(initial={
            'nombre_cliente': salida.nombre_cliente,
            'especie': salida.especie,
            'cantidad_kg': salida.cantidad_kg,
            'cantidad_caja': salida.cantidad_caja,
            'precio_kg': salida.precio_kg,
            'precio_caja': salida.precio_caja,
        })
    return render(request, 'RegistroSalidas.html', {'form': form, 'id_salida': id_salida})

@login_required
def Entradas(request):
    data=request.POST.get('fecha')
    try:
        datos=data
        entr=Entrada.objects.filter(fecha=datos)
        data=[(obj.id,obj.nombre_proveedor,obj.especie,obj.cantidad_kg,obj.cantidad_caja,obj.precio_kg, obj.precio_caja,obj.fecha) for obj in entr]
    except:
        data=data
    return render(request,'Entradas.html',{
        'data':data
    })
@login_required
def Salidas(request):
    salida=request.POST.get('fecha')
    try:
        datos=salida
        sald=Salida.objects.filter(fecha=datos)
        salida=[(obj.id,obj.nombre_cliente,obj.especie,obj.cantidad_kg,obj.cantidad_caja,obj.precio_kg, obj.precio_caja,obj.fecha) for obj in sald]
    except:
        salida=salida
    return render(request,'Salidas.html',{
        'salida':salida
    })

