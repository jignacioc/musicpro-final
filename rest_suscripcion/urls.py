from django.urls import path
from rest_suscripcion.views import lista_suscriptores, suscripcion_detalles

urlpatterns = [
    path('lista_suscriptores', lista_suscriptores, name="lista suscriptores"),
    path('suscripcion_detalles/<id>', suscripcion_detalles, name='suscripcion_detalles')
]