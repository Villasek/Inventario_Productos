from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import producto
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoForm

def home(request):
    return HttpResponse("<h1> ¡Bienvenido al sistema de inventario </h1>")

def lista_productos(request):
    productos = producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos':productos})


#crear producto 

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else: 
        form = ProductoForm()
        return render(request, 'inventario/from_producto.html', {'form':form})
    
#Editar producto

def editar_producto(request,pk):
    producto = get_object_or_404(producto, pk=pk)
    if request.method =='POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'inventario/form_producto.html', {'form':form})
    
#Eliminar producto

def eliminar_producto(request, pk):
    producto = get_object_or_404(producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect ('lista_productos')
    return render(request, 'inventario/confirmar_eliminar.html', {'producto':producto})
