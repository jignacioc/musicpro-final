from django.db import models

# Create your models here.
class Suscriptores (models.Model):
    correo = models.CharField(primary_key=True,max_length=55,  verbose_name='pk suscriptor')
    id_suscripcion = models.IntegerField( verbose_name='id ssuscripcion')
    estado = models.BooleanField(default=False ,verbose_name='estado sc')
    def str(self):
        return self.correo