from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class CarritoCompra(models.Model):
class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    totalCarrito = models.IntegerField(verbose_name='Total', null=True, blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=True, blank=True)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return self.idCarrito


class Descuento(models.Model):
    idDescuento = models.AutoField(primary_key=True)
    nombreDescuento = models.CharField(max_length=100, verbose_name='Nombre descuento')
    descripcion = models.CharField(max_length=254, verbose_name='Descripción descuento')
    porcentajeDescuento = models.IntegerField(verbose_name='porcentajeDescuento')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'

    def __str__(self):
        return self.nombreDescuento


class CategoriaProducto(models.Model):
    idCategoriaProducto = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100, verbose_name='Nombre categoria')

    class Meta:
        verbose_name = 'Categoria producto'
        verbose_name_plural = 'Categorias productos'

    def __str__(self):
        return self.nombreCategoria


class ProductoPublico(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=254, verbose_name='Descripción')
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio')
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(verbose_name='Stock disponible')
    imagen = models.ImageField(upload_to='ventas', null=True, blank=True,verbose_name='Imagen')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Producto Publico'
        verbose_name_plural = 'Productos Publicos'
    
    def __str__(self):
        return self.nombreProducto


class ItemCarrito(models.Model):
    idItemCarrito = models.AutoField(primary_key=True)
    cantidad  = models.IntegerField(verbose_name='Cantidad')
    producto = models.ForeignKey(ProductoPublico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item del carrito'
        verbose_name_plural = 'Items del carrito'
    
    def __str__(self):
        return self.idItemCarrito


class DetallePedido(models.Model):
    idDetallePedido = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.idDetallePedido)
    
    @property
    def get_total_cart(self):
        itemspedido = self.itemspedido_set.all()
        total = sum([item.get_total for item in itemspedido])
        return total



class ItemsPedido(models.Model):
    idItemsPedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(ProductoPublico, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    detallePedido = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Item del pedido'
        verbose_name_plural = 'Items del pedido'
    
    def __str__(self):
        return str(self.idItemsPedido)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

    @property
    def get_stock(self):
        number_list = list(range(1,self.producto.stock+1))
        return number_list