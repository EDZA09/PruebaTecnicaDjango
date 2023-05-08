from django.db import models
from django.contrib.auth.models import User

#* Modelo de Usuario
  
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    #models.t
    boton1 = models.IntegerField(default=0)
    boton2 = models.IntegerField(default=0)

    def __str__(self):
        return '{0},{1}'.format(self.usuario.last_name,self.usuario.first_name)

