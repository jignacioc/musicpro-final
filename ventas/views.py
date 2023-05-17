from django.shortcuts import render
from .models import * 
from .forms import ItemCarritoForm
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def carrito(request):
    if request.user.is_authenticated:
        user = request.user
        detallePedido, created = DetallePedido.objects.get_or_create(usuario=user)
        items = detallePedido.itemspedido_set.all()
    else:
        items = []
        detallePedido = {'get_total_cart': 0}

    context = {'items': items, 'detallePedido':detallePedido}
    return render(request, 'ventas/carrito.html', context)

@login_required
def vista_productos_publicos(request):

    user = request.user
    detallePedido, created = DetallePedido.objects.get_or_create(usuario=user)
    items = detallePedido.itemspedido_set.all()
    
    productos = ProductoPublico.objects.all()

    data = {
        'productos': productos,
        'form': ItemCarritoForm
    }

    if request.method == 'POST':
        formulario = ItemCarritoForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'ventas/productos_publicos.html', data)

def agregarProducto(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:', productId)
    print('Action:', action)

    user = request.user.id
    product = ProductoPublico.objects.get(idProducto=productId)

    pedido, created = DetallePedido.objects.get_or_create(usuario=user)

    itemPedido, created = ItemsPedido.objects.get_or_create(detallePedido=pedido, producto=product)

    if action == 'add':
        itemPedido.cantidad = (itemPedido.cantidad + 1)
    elif action == 'remove':
        itemPedido.cantidad = (itemPedido.cantidad - 1)
    elif action == 'delete':
        itemPedido.cantidad = 0

    itemPedido.save()

    if itemPedido.cantidad <= 0:
        itemPedido.delete()
    return JsonResponse('Producto añadido', safe=False)

