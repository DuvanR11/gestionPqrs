from django.db import models
from django.contrib.auth.models import AbstractUser
from alcaldia import settings
from django.conf import settings



# Create from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    oficina = models.ForeignKey('oficina', on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField('foto para tu perfil', upload_to='peril/', blank=True, null=True)

   

class Pqr(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    correo = models.EmailField(max_length=20,  blank=True, null=True)
    titulo = models.CharField(max_length=30,  blank=True, null=True)
    oficina = models.ForeignKey('oficina', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to = "pqrs/")
    fechaRegistro = models.DateTimeField(auto_now = True)
    fechaRespuesta = models.DateTimeField(auto_now = True)
    estado = models.BooleanField(default=True)
    barrio = models.CharField(max_length=50,  blank=True, null=True)
    anonima = models.BooleanField(default=False)
    
    def __str__(self):
        return self.codigo, self.estado, self.titulo
    
   
    
class Oficina(models.Model):
    id = models.AutoField(primary_key=True)
    nombreOficina = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombreOficina
    
