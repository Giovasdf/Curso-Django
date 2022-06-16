from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="id de Categoria")
    nombreCategoria = models.CharField(max_length=70,verbose_name="Nombre del Categoria")
    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True,verbose_name="id de Producto")
    nombreProducto = models.CharField(max_length=80,verbose_name="Nombre del producto")
    valorProducto = models.IntegerField(verbose_name="Valor de Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreProducto