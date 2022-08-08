from django.contrib import admin
from pqrs.models import *
# Register your models here.
class PqrAdmin(admin.ModelAdmin):
    list_display =["id", "codigo", "correo", "titulo", "oficina", "archivo", "fechaRegistro", "fechaRespuesta", "estado", "barrio", "anonima"]
    search_fields =["codigo"]
    list_filter = ('oficina', 'fechaRegistro', 'estado')
    
class OficinasAdmin(admin.ModelAdmin):
    list_display =["id", "nombreOficina"]
    search_fields =["nombreOficina"]
     
class UsuarioAdmin(admin.ModelAdmin):
    list_display =["id", "username", "email", "oficina", "imagen", "is_superuser"]
    search_fields =["id"]
    
admin.site.register(Pqr, PqrAdmin)
admin.site.register(Oficina, OficinasAdmin)
admin.site.register(Usuario, UsuarioAdmin)
