from django.urls import path
from .views import lista_producto,detalle_producto

urlpatterns = [
    path('lista-producto',lista_producto,name="lista_producto"),
    path('detalle-producto/<id>',detalle_producto, name="detalle_producto")

]